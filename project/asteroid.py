"""
이거 존나 재밌겠다 하악하악
일단 점점점을 존나 그려서 png파일로 해가지고 존나 예쁘게 꾸미는겨
교수새기가 존나 '디자인적 요소'본다했으니까 존나 꾸며야지
존나 보너스 게임같은 룰도 넣으면 차별화되지 않을까
예를 들면 가끔나오는 보물상자 먹으면 존나 스코어 뿌리고
스코어 뿌릴 때 이벤트 창 나오고!
레벨로 단계만들고!

가. 애스터로이드 게임
"""
import turtle
import random

t=turtle.Turtle()
t.shape("turtle")
# 터틀 생성 없이 네모 그릴 수 있는지도 확인
a=turtle.Turtle()
a.up()
a.goto(-200,200)
a.down()
for i in range(3):
a.fd(200)
a.rt(90)
"""
*터틀은 방향키로 움직일 수 있음
*터틀이 네모칸을 벗어날 수 없음
"""
turtle.speed=5
score=0
while True:
네모칸 안에 무작위로 점을 생성함


나. 애니메이션 만들기
다. my paint 기능 확장하기
