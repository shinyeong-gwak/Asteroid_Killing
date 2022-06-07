import turtle

screen_title = ".\\images\\title.gif"
sel_start = ".\\images\\title_start.gif"
back_screen = ".\\images\\screen.gif"
#터틀 창크기 지정
turtle.setup(width=1000,height=600,startx=300,starty=100)
#입력받음
s = turtle.Screen()

s.addshape(screen_title)
s.addshape(sel_start)
s.addshape(back_screen)

bground = turtle.Turtle()
bground.shape(screen_title)
bground.stamp()