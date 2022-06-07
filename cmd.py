import turtle

#터틀 창에 그려진 정보 삭제, 스크린의 모든 터틀 숨김
def clear_screen():
    turtle.resetscreen()
    for i in turtle.Screen().turtles():
        i.shape("classic")
        i.hideturtle()

