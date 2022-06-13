# 1. 눈사람을 그리는 함수를 작성하고 이 함수를 여러번 호출하여 랜덤한 위치에 눈사람을 그리는 프로그램을 작성하라.
#    draw_snowman(x, y) 함수를 작성하고 테스트, 터틀 그래픽에서 배경을 하늘색으로 변경하려면 s = turtle.Screen();
#    s.bgcolor("skyblue"); 로 처리한다.

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("black", "white")
s = turtle.Screen(); s.bgcolor("skyblue");

def draw_snowman(x, y):
    t.up()
    t.goto(x, y)
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.goto(x, y-25)
    t.setheading(135)
    t.forward(50)
    t.backward(50)
    
    t.setheading(30)
    t.forward(50)
    t.backward(50)
    t.setheading(0)
    
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.goto(x, y-70)
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    
draw_snowman(0, 0)
draw_snowman(100, 0)
draw_snowman(200, 0)
t._screen.exitonclick()

# 2. 6각형을 그리는 draw_hexa()함수를 작성하고 이 함수를 호출하여 제공한 연습문제 문서의 그림, 벌집 모양을 
#    화면에 그려보는 프로그램을 작성하라.

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def hexagon():
    for i in range(6):
        turtle.fd(100)
        turtle.left(360/6)
    for i in range (6):
        hexagon()
        t.fd(100)
        t.right(60)    
t._screen.exitonclick()
