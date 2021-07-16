# -*- coding: utf-8 -*-
import os

def create_item_cap(id, username, about_me):
    try:
        os.mkdir('cap/' + id +'/' + username)
    except OSError:
        print("Создать директорию не удалось")
    file_me = open('cap/' + id + '/' + username + '/' + 'about_me.txt', 'w')
    file_me.write(about_me)
    file_me.close()

def dop_cap(id, username, about_team):
    file_team = open('cap/'+ id + '/' + username + '/' + 'about_team.txt', 'w')
    file_team.write(about_team)
    file_team.close()

def create_item_member(id, username, about_me):
    try:
        os.mkdir('member/'+ id +'/' + username)
    except OSError:
        print("Создать директорию не удалось")
    file_me = open('member/' + id +'/' + username + '/' + 'about_me.txt', 'w')
    file_me.write(about_me)
    file_me.close()


