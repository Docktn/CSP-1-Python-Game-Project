# Stuart Hamilton
# 10-31-22
# Period 1
# THE BOMBER

from turtle import *
from random import *
from time import *

#~VARIABLES~#

player = Turtle()
enemy = Turtle()
timeStart = time()
name = ""
score = 0

#~FUNCTIONS~#

def win():
    print("-------------------")
    print(name, "'S SCORE IS", score)
    if score > 10000:
        print(name, "WON! \u263A")
    elif score > 7500:
        print("SO CLOSE!")
    else:
        print("THE ENEMY WON!")
                
def greet():
    print("~~~~~~~THE BOMBER~~~~~~~")
    print("CONTROLS: \n w & s = FORWARD & BACK \n a & d = LEFT & RIGHT \n F = BOOSTER")
    print("CAPITALS MATTER!")
    print("TRY YOUR BEST TO AVOID THE BOMBS WHEN THEY EXPLODE")
    print("IF YOU SCORE OVER 10000 POINTS YOU WIN!")
    name = input("ENTER YOUR NAME TO BEGIN: ")
       
def settings(turt):
    bgcolor('black')
    player.pencolor('white')
    player.speed(0)
    turt.speed(5)
    turt.pencolor('black')
    turt.hideturtle()
    player.penup()
    for n in range(50):
        setup(10*n, n*10)
        
def go(turt, x, y):
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    
def reBound():
    if player.ycor() > 250:
        go(player, player.xcor(), player.ycor() - 500)
    if player.ycor() < -250:
        go(player, player.xcor(), player.ycor() + 500)
    if player.xcor() > 250:
        go(player, player.xcor() - 500, player.ycor())
    if player.xcor() < -250:
        go(player, player.xcor()+ 500, player.ycor())
    player.pu()
    
def plantBomb(turt):
    turt.circle(5)
def goRandom(turt):
    randX = randint(-250,250)
    randY = randint(-250,250)
    go(turt,randX,randY)
        
def colCircle(fc, size, turt):
    turt.pencolor(fc)
    turt.fillcolor(fc)
    turt.begin_fill()
    turt.circle(size)
    turt.end_fill()
    turt.pencolor('white')
    
def detonate(turt):
    bombsize = randint(100,150)
    circTop = turt.ycor() + bombsize
    circLeft = turt.xcor() - bombsize
    circBottom = turt.ycor() - bombsize
    circRight = turt.xcor() + bombsize

    crdY = player.ycor()
    crdX = player.xcor()

    turt.speed(0)

    go(turt, turt.xcor(), turt.ycor()-bombsize-5)
    colCircle('red', bombsize, turt)
    sleep(.01)
    if crdY > circBottom and crdY < circTop and crdX < circRight and crdX > circLeft:
        bye()
        timeEnd = time()
        score = int(timeEnd - timeStart) * 256 + randint(1,10)
        win()
    go(turt, turt.xcor(), turt.ycor() - bombsize)
    colCircle('black', bombsize*50, turt)
    turt.speed(5)

def spawnEnemy(turt):
    go(turt, 50, 50)
    settings(turt)
    enemyAct(turt)
    
def bckwd():
    player.backward(25)
    reBound()
def turnLeft():
    player.left(45)
def turnRight():
    player.right(45)
def forwd():
    player.forward(25)
    reBound()
def booster():
    for n in range(5):
        player.forward(25)
        reBound()

def enemyAct(turt):
    while True:
        goRandom(enemy)
        plantBomb(enemy)

        detonate(enemy)

#~MAIN CODE~#
        
greet()
listen()

onkey(forwd, 'w')
onkey(turnRight, 'd')
onkey(turnLeft, 'a')
onkey(bckwd, 's')
onkey(booster, 'F')

spawnEnemy(enemy)
