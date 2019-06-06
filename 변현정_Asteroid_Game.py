# -*- coding: utf-8 -*-
#변현정 1976185

import turtle
import random
import time

player = turtle.Turtle()  #우주선
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)

a1 = turtle.Turtle()      #소행성1
a1.color("red")
a1.shape("circle")
a1.penup()
a1.speed(0)
a1.goto(random.randint(-300,300), random.randint(-300,300))

a2 = turtle.Turtle()      #소행성2
a2.color("yellow")
a2.shape("circle")
a2.penup()
a2.speed(0)
a2.goto(random.randint(-300,300),random.randint(-300,300))

screen = turtle.Screen()

crasheda1 = False
crasheda2 = False


### --- Functions --- ###


def turnleft():
    player.left(30)  #왼쪽으로 30도 회전한다.

def turnright():
    player.right(30) #오른쪽으로 30도 회전한다. 

speed = 2

def speedUp():
    global speed
    speed += 1
    if speed == 5:
        speed = 2

screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(speedUp,"space")
screen.listen() #거북이 그래픽 창이 키보드 입력을 받는다.

def play():
    player.forward(speed) #2픽셀 전진
    if crasheda1 == False:
        a1.forward(2)
    if crasheda2 == False:
        a2.forward(2)
    checkPosition()
    checkCrash()
    if gameOver() == False:
        screen.ontimer(play,10) #10ms가 지나면 play()를 호출한다.

def checkPosition():
    #소행성과 사용자의 위치가 범위를 벗어났을 때 그 위치를 조정하는 함수
    #소행성(a1,a2)는 오른쪽으로만 진행하므로 x좌표만 검사
    if a1.xcor()>500:
        a1.goto(random.randint(-300,300), random.randint(-300,300))
    if a2.xcor()>500:
        a2.goto(random.randint(-300,300), random.randint(-300,300))
    if player.xcor()<-500 or player.xcor()>500 or player.ycor()<-500 or player.ycor()>500:
        player.goto(0,0)
        #우주선은 원점으로 오게 한다.
    

def checkCrash():
    global crasheda1
    global crasheda2
    
    if player.distance(a1)<12:
        a1.color("black")
        crasheda1 = True 
    if player.distance(a2)<12:
        a2.color("black")
        crasheda2 = True 

def gameOver():
    if crasheda1 == True and crasheda2 == True:
        end = time.time()
        et = end - start
        player.write("GameOver : %0.2f"%et, False, "center", ("Arial",15, "bold"))
        return True
    else:
        return False

### --- Main Screen --- ###


#10ms 후 부터 게임을 시작하도록 설정한다.
start = time.time()

screen.ontimer(play, 10) #10ms가 지나면 play()를 호출한다.




