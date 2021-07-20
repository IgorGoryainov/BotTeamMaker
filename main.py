# -*- coding: utf-8 -*-
import telebot
import data_base as db
import shutil
import os
from telebot import types
bot = telebot.TeleBot('token')

user_list = []

with open(r"user_list.txt", "r") as file:
    for line in file:
        user_list.append(line)
user_list = [line.rstrip() for line in user_list]

@bot.message_handler(commands=['start'])
def start(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_cap = types.InlineKeyboardButton(text='Капитан', callback_data='cap')
    item_member = types.InlineKeyboardButton(text='Командный игрок', callback_data='member')
    markup_inline.add(item_cap)
    markup_inline.add(item_member)
    bot.send_message(message.chat.id, 'Я -', reply_markup=markup_inline)


@bot.message_handler(commands=['delete'])
def delete(message):
    if user_list.count(str(message.from_user.id)) == 0:
        bot.send_message(message.chat.id, 'У тебя нет заявки. Создай новую: напиши /start', reply_markup=types.ReplyKeyboardRemove())
    else:
        while user_list.count(str(message.from_user.id)) != 0:
            user_list.remove(str(message.from_user.id))
        for i in range(1, 4):
            cap_list = os.listdir('cap/' + str(i))
            if cap_list.count(str(message.from_user.id)) != 0:
                shutil.rmtree('cap/' + str(i) + '/' + str(message.from_user.id))
        for i in range(1, 4):
            member_list = os.listdir('member//' + str(i))
            if member_list.count(str(message.from_user.id)) != 0:
                shutil.rmtree('member/' + str(i) + '/' + str(message.from_user.id))

        with open(r"user_list.txt", "w") as file:
            for line in user_list:
                file.write(line + '\n')
        bot.send_message(message.chat.id, 'Запись успешно удалена', reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Чтобы создать заявку - /start, удалить - /delete")
    elif message.text == 'Обновить список участников #1':
        member_list = os.listdir('member/1')
        mes = ''
        for user in member_list:
            mes += '@' + user + '\nО себе: '
            file = open('member/1/' + user + '/' + 'about_me.txt')
            mes += file.read()
            mes += '\n\n'
            file.close()
        bot.send_message(message.chat.id, 'Список участников:\n\n' + mes)
    elif message.text == 'Обновить список участников #2':
        member_list = os.listdir('member/2')
        mes = ''
        for user in member_list:
            mes += '@' + user + '\nО себе: '
            file = open('member/2/' + user + '/' + 'about_me.txt')
            mes += file.read()
            mes += '\n\n'
            file.close()
        bot.send_message(message.chat.id, 'Список участников:\n\n' + mes)
    elif message.text == 'Обновить список участников #3':
        member_list = os.listdir('member/3')
        mes = ''
        for user in member_list:
            mes += '@' + user + '\nО себе: '
            file = open('member/3/' + user + '/' + 'about_me.txt')
            mes += file.read()
            mes += '\n\n'
            file.close()
        bot.send_message(message.chat.id, 'Список участников:\n\n' + mes)
    elif message.text == 'Обновить список команд #1':
        member_list = os.listdir('cap/1')
        mes = ''
        for user in member_list:
            mes += '@' + user + '\nО капитане: '
            file = open('cap/1/' + user + '/' + 'about_me.txt')
            mes += file.read()
            file.close()
            file = open('cap/1/' + user + '/' + 'about_team.txt')
            mes += '\nВ команду нужны: '
            mes += file.read()
            mes += '\n\n'
            file.close()
        bot.send_message(message.chat.id, 'Список команд:\n\n' + mes)
    elif message.text == 'Обновить список команд #2':
        member_list = os.listdir('cap/2')
        mes = ''
        for user in member_list:
            mes += '@' + user + '\nО капитане: '
            file = open('cap/2/' + user + '/' + 'about_me.txt')
            mes += file.read()
            file.close()
            file = open('cap/2/' + user + '/' + 'about_team.txt')
            mes += '\nВ команду нужны: '
            mes += file.read()
            mes += '\n\n'
            file.close()
        bot.send_message(message.chat.id, 'Список команд:\n\n' + mes)
    elif message.text == 'Обновить список команд #3':
        member_list = os.listdir('cap/3')
        mes = ''
        for user in member_list:
            mes += '@' + user + '\nО капитане: '
            file = open('cap/3/' + user + '/' + 'about_me.txt')
            mes += file.read()
            file.close()
            file = open('cap/3/' + user + '/' + 'about_team.txt')
            mes += '\nВ команду нужны: '
            mes += file.read()
            mes += '\n\n'
            file.close()
        bot.send_message(message.chat.id, 'Список команд:\n\n' + mes)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start , чтобы создать заявку и /delete - удалить")

def get_about_cap_1(message):
    text = message.text
    bot.send_message(message.chat.id, "Кого ты ищешь:")
    db.create_item_cap('1', str(message.from_user.id), text)
    user_list.append(str(message.from_user.id))
    with open(r"user_list.txt", "w") as file:
        for line in user_list:
            file.write(line + '\n')
    file.close()
    bot.register_next_step_handler(message, get_about_team_1)

def get_about_team_1(message):
    text = message.text
    db.dop_cap('1', str(message.from_user.id), text)
    bot.send_message(message.chat.id, "Отлично! Твоя зявка создана. Теперь ее могут увидеть все участники")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Обновить список участников #1')
    bot.send_message(message.chat.id, "Список участников, желающих вступить в команду по твоему кейсу:", reply_markup=keyboard)
    member_list = os.listdir('member/1')
    mes = ''
    for user in member_list:
        mes += '@' + user + '\nО себе: '
        file = open('member/1/' + user + '/' + 'about_me.txt')
        mes += file.read()
        mes += '\n\n'
        file.close()
    bot.send_message(message.chat.id, mes)

def get_about_cap_2(message):
    text = message.text
    bot.send_message(message.chat.id, "Кого ты ищешь:")
    db.create_item_cap('2', str(message.from_user.id), text)
    user_list.append(str(message.from_user.id))
    with open(r"user_list.txt", "w") as file:
        for line in user_list:
            file.write(line + '\n')
    file.close()
    bot.register_next_step_handler(message, get_about_team_2)

def get_about_team_2(message):
    text = message.text
    db.dop_cap('2', str(message.from_user.id), text)
    bot.send_message(message.chat.id, "Отлично! Твоя зявка создана. Теперь ее могут увидеть все участники")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Обновить список участников #2')
    bot.send_message(message.chat.id, "Список участников, желающих вступить в команду по твоему кейсу:",
                     reply_markup=keyboard)
    member_list = os.listdir('member/2')
    mes = ''
    for user in member_list:
        mes += '@' + user + '\nО себе: '
        file = open('member/2/' + user + '/' + 'about_me.txt')
        mes += file.read()
        mes += '\n\n'
        file.close()
    bot.send_message(message.chat.id, mes)

def get_about_cap_3(message):
    text = message.text
    bot.send_message(message.chat.id, "Кого ты ищешь:")
    db.create_item_cap('3', str(message.from_user.id), text)
    user_list.append(str(message.from_user.id))
    with open(r"user_list.txt", "w") as file:
        for line in user_list:
            file.write(line + '\n')
    file.close()
    bot.register_next_step_handler(message, get_about_team_3)

def get_about_team_3(message):
    text = message.text
    db.dop_cap('3', str(message.from_user.id), text)
    bot.send_message(message.chat.id, "Отлично! Твоя зявка создана. Теперь ее могут увидеть все участники")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Обновить список участников #3')
    bot.send_message(message.chat.id, "Список участников, желающих вступить в команду по твоему кейсу:",
                     reply_markup=keyboard)
    member_list = os.listdir('member/3')
    mes = ''
    for user in member_list:
        mes += '@' + user + '\nО себе: '
        file = open('member/3/' + user + '/' + 'about_me.txt')
        mes += file.read()
        mes += '\n\n'
        file.close()
    bot.send_message(message.chat.id, mes)

def get_about_me_1(message):
    text = message.text
    db.create_item_member('1', str(message.from_user.id), text)
    user_list.append(str(message.from_user.id))
    with open(r"user_list.txt", "w") as file:
        for line in user_list:
            file.write(line + '\n')
    file.close()
    bot.send_message(message.chat.id, "Отлично! Твоя зявка создана. Теперь ее могут увидеть все участники")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Обновить список команд #1')
    bot.send_message(message.chat.id, "Список команд, в которые ты можешь вступить:", reply_markup=keyboard)
    member_list = os.listdir('cap/1')
    mes = ''
    for user in member_list:
        mes += '@' + user + '\nО капитане: '
        file = open('cap/1/' + user + '/' + 'about_me.txt')
        mes += file.read()
        file.close()
        file = open('cap/1/' + user + '/' + 'about_team.txt')
        mes += '\nВ команду нужны: '
        mes += file.read()
        mes += '\n\n'
        file.close()
    bot.send_message(message.chat.id, mes)

def get_about_me_2(message):
    text = message.text
    db.create_item_member('2', str(message.from_user.id), text)
    user_list.append(str(message.from_user.id))
    with open(r"user_list.txt", "w") as file:
        for line in user_list:
            file.write(line + '\n')
    file.close()
    bot.send_message(message.chat.id, "Отлично! Твоя зявка создана. Теперь ее могут увидеть все участники")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Обновить список команд #2')
    bot.send_message(message.chat.id, "Список команд, в которые ты можешь вступить:", reply_markup=keyboard)
    member_list = os.listdir('cap/2')
    mes = ''
    for user in member_list:
        mes += '@' + user + '\nО капитане: '
        file = open('cap/2/' + user + '/' + 'about_me.txt')
        mes += file.read()
        file.close()
        file = open('cap/2/' + user + '/' + 'about_team.txt')
        mes += '\nВ команду нужны: '
        mes += file.read()
        mes += '\n\n'
        file.close()
    bot.send_message(message.chat.id, mes)

def get_about_me_3(message):
    text = message.text
    db.create_item_member('3', str(message.from_user.id), text)
    user_list.append(str(message.from_user.id))
    with open(r"user_list.txt", "w") as file:
        for line in user_list:
            file.write(line + '\n')
    file.close()
    bot.send_message(message.chat.id, "Отлично! Твоя зявка создана. Теперь ее могут увидеть все участники")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Обновить список команд #3')
    bot.send_message(message.chat.id, "Список команд, в которые ты можешь вступить:", reply_markup=keyboard)
    member_list = os.listdir('cap/3')
    mes = ''
    for user in member_list:
        mes += '@' + user + '\nО капитане: '
        file = open('cap/3/' + user + '/' + 'about_me.txt')
        mes += file.read()
        file.close()
        file = open('cap/3/' + user + '/' + 'about_team.txt')
        mes += '\nВ команду нужны: '
        mes += file.read()
        mes += '\n\n'
        file.close()
    bot.send_message(message.chat.id, mes)

def choose_directional_cap(call):
    markup_inline = types.InlineKeyboardMarkup()
    item_angel = types.InlineKeyboardButton(text='Креативный бизнес-ангел', callback_data='angel_cap')
    item_tavrida = types.InlineKeyboardButton(text='Арт-кластер “Таврида”', callback_data='tavrida_cap')
    item_robot = types.InlineKeyboardButton(text='Коллаборативная робототехника', callback_data='robot_cap')
    markup_inline.add(item_angel)
    markup_inline.add(item_tavrida)
    markup_inline.add(item_robot)
    bot.send_message(call.message.chat.id, "Выбери кейс, в котором ты участвуешь:", reply_markup=markup_inline)

def choose_directional_member(call):
    markup_inline = types.InlineKeyboardMarkup()
    item_angel = types.InlineKeyboardButton(text='Креативный бизнес-ангел', callback_data='angel_member')
    item_tavrida = types.InlineKeyboardButton(text='Арт-кластер “Таврида”', callback_data='tavrida_member')
    item_robot = types.InlineKeyboardButton(text='Коллаборативная робототехника', callback_data='robot_member')
    markup_inline.add(item_angel)
    markup_inline.add(item_tavrida)
    markup_inline.add(item_robot)
    bot.send_message(call.message.chat.id, "Выбери кейс, в котором ты участвуешь:", reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "cap":
        if user_list.count(call.message.chat.id) == 0:
            choose_directional_cap(call)
        else:
            bot.send_message(call.message.chat.id, "Удали свою предыдущую заявку, командой /delete")
        bot.answer_callback_query(call.id)
    elif call.data == "member":
        if user_list.count(call.message.chat.id) == 0:
            choose_directional_member(call)
        else:
            bot.send_message(call.message.chat.id, "Удали свою предыдущую заявку, командой /delete")
        bot.answer_callback_query(call.id)
    elif call.data == "angel_cap":
        if user_list.count(call.message.chat.id) == 0:
            bot.send_message(call.message.chat.id, "Расскажи о себе: (В начале укажи свой username в telegram)")
            bot.register_next_step_handler(call.message, get_about_cap_1)
        else:
            bot.send_message(call.message.chat.id, "Удали свою предыдущую заявку, командой /delete")
        bot.answer_callback_query(call.id)
    elif call.data == "tavrida_cap":
        if user_list.count(call.message.chat.id) == 0:
            bot.send_message(call.message.chat.id, "Расскажи о себе: (В начале укажи свой username в telegram)")
            bot.register_next_step_handler(call.message, get_about_cap_2)
        else:
            bot.send_message(call.message.chat.id, "Удали свою предыдущую заявку, командой /delete")
        bot.answer_callback_query(call.id)
    elif call.data == "robot_cap":
        if user_list.count(call.message.chat.id) == 0:
            bot.send_message(call.message.chat.id, "Расскажи о себе: (В начале укажи свой username в telegram)")
            bot.register_next_step_handler(call.message, get_about_cap_3)
        else:
            bot.send_message(call.message.chat.id, "Удали свою предыдущую заявку, командой /delete")
        bot.answer_callback_query(call.id)
    elif call.data == "angel_member":
        if user_list.count(call.message.chat.id) == 0:
            bot.send_message(call.message.chat.id, "Расскажи о себе: (В начале укажи свой username в telegram)")
            bot.register_next_step_handler(call.message, get_about_me_1)
        else:
            bot.send_message(call.message.chat.id, "Удали свою предыдущую заявку, командой /delete")
        bot.answer_callback_query(call.id)
    elif call.data == "tavrida_member":
        if user_list.count(call.message.chat.id) == 0:
            bot.send_message(call.message.chat.id, "Расскажи о себе: (В начале укажи свой username в telegram)")
            bot.register_next_step_handler(call.message, get_about_me_2)
        else:
            bot.send_message(call.message.chat.id, "Удали свою предыдущую заявку, командой /delete")
        bot.answer_callback_query(call.id)
    elif call.data == "robot_member":
        if user_list.count(call.message.chat.id) == 0:
            bot.send_message(call.message.chat.id, "Расскажи о себе: (В начале укажи свой username в telegram)")
            bot.register_next_step_handler(call.message, get_about_me_3)
        else:
            bot.send_message(call.message.chat.id, "Удали свою предыдущую заявку, командой /delete")
        bot.answer_callback_query(call.id)


bot.polling(none_stop=True, interval=0)
