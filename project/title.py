import turtle
import button
import cmd
from bground import *
from All_Game import All_Game

def go_title():

    def start_select(x, y):
        cmd.clear_screen()
        select_player()

    def setting(x,y):
        print('색상 설정')

    def exit(x, y):
        print('게임 종료')
        turtle.bye()

    title_button = [
        button.Button(yco=20,mes="게임 시작"),
        button.Button(yco=-60,mes="설정"),
        button.Button(yco=-140,mes="게임 종료")
    ]
    #버튼 동작 지정, 버튼 글씨 지정(이거 한줄로 하고싶은데,,)
    title_button[0].func(start_select)
    title_button[1].func(setting)
    title_button[2].func(exit)
    for i in title_button:
        i.write()

def select_player():
    bground.shape(sel_start)
    bground.stamp()

    sel_button = [
        button.Button(yco=80,mes="1p"),
        button.Button(yco=0,mes="2p")
    ]

    sel_button[0].func(game_1p)#1p로 게임 시작
    #sel_button[1].func()#2p로 게임 시작


def game_1p(x,y):
    cmd.clear_screen()
    bground.shape(back_screen)
    bground.stamp()
    All_Game()###########얘는 정리하면 바꿀거

