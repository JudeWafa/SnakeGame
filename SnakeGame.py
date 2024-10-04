#!/usr/bin/env python3


import turtle
import time
from random import randint
from math import ceil

window = turtle.Screen()
window.setup(640,640)
window.bgcolor('yellow')
window.tracer(0)
window.title("Snake Game By Jood Wafa")

score = 0
high = 0
delay = 0.1
x = 0
y = 0


start_time = time.perf_counter()
head = turtle.Turtle()
head.shape('square')
head.speed(0)
head.penup()
head.goto(-300,300)
head.color("black")
head.pendown()
head.pensize(65)
head.forward(600)
head.penup()
head.direction = "stop"
head.goto(0,0)
head.color("black")
# BC0F16
scr = turtle.Turtle()
scr.speed(0)
scr.penup()
scr.hideturtle()
scr.goto(0,270)
scr.color("white")
scr.write("Score: {}  High Score: {}".format(score,high), move=False, align="center", font=('Futura',30,'bold'))

fruit = turtle.Turtle()
fruit.shape("circle")
fruit.color("#66023c")
fruit.hideturtle()
fruit.penup()
fruit.speed(0)
fruit.goto(randint(-300,300), randint(-300,260))


body = []
blocks = []


	
def move_up():
	if head.direction != "down":
		head.direction = "up"
		head.sety(head.ycor()+20)
def move_left():
	if head.direction != "right":
		head.direction = "left"
		head.setx(head.xcor()-20)
def move_down():
	if head.direction != "up":
		head.sety(head.ycor()-20)
		head.direction = "down"
def move_right():
	if head.direction != "left":
		head.direction = "right"
		head.setx(head.xcor()+20)

def up():
	if head.direction != "down":
		head.direction = "up"
def down():
	if head.direction != "up":
		head.direction = "down"
def left():
	if head.direction != "right":
		head.direction = "left"
def right():
	if head.direction != "left":
		head.direction = "right"

def setfruit():
	x = randint(-300,300)
	y = randint(-300,260)
	fruit.goto(x,y)
	for b in blocks:
		if fruit.distance(b) < 20:
			x = randint(-300,300)
			y = randint(-300,260)
	


def update_score():
	scr.clear()
	scr.write("Score: {}  High Score: {}".format(score,high), move=False, align="center", font=('Futura',30,'bold'))

window.listen()
window.onkeypress(up, "Up")
window.onkeypress(up, "w")
window.onkeypress(left, "Left")
window.onkeypress(left, "a")
window.onkeypress(down, "Down")
window.onkeypress(down, "s")
window.onkeypress(right, "Right")
window.onkeypress(right, "d")

def restart():
	global score
	global delay
	score = 0
	time.sleep(1)
	head.goto(0,0)
	for b in body:
		b.hideturtle()
	body.clear()
	started = False
	scr.clear()
	scr.write("Score: {}  High Score: {}".format(score,high), move=False, align="center", font=('Futura',30,'bold'))
	head.direction = "stop"
	delay = 0.1

def move():
	for i in range(len(body)-1,0,-1):
		x = body[i-1].xcor()
		y = body[i-1].ycor()
		body[i].goto(x, y)
	if len(body) > 0:
		x = head.xcor()
		y = head.ycor()
		body[0].goto(x,y)
	if head.direction == "up":
		move_up()
	elif head.direction == "down":
		move_down()
	elif head.direction == "left":
		move_left()
	elif head.direction == "right":
		move_right()

k = 0.001


while(True):
	window.update()
	
	if head.ycor()>260 or head.ycor()<-300 or head.xcor()>300 or head.xcor()<-320:
		restart()

	for b in body:
		if b.xcor() == head.xcor() and b.ycor() == head.ycor():
			restart()
			break

	for b in blocks:
		if head.distance(b)<20:
			restart()
			break

	if head.distance(fruit)<20:
		score+=10
		if score > high:
			high = score 
		delay-=0.001
		setfruit()
		update_score()
		s = turtle.Turtle()
		s.penup()
		s.speed(0)
		s.color("grey")
		s.shape("square")
		body.append(s)

	move()
	
	fruit.showturtle()
	end_time = time.perf_counter()
	elapsed_time = ceil(end_time - start_time)
	
	k = randint(-1000,1000)
	if k%27 == 0 and k%4 == 0 and score!=0:
		x = randint(-300,300)
		y = randint(-300,260)
		if x >10 or x<-10 and y>10 or y<-10:
			f = turtle.Turtle()
			f.shape("square")
			f.speed(0)
			f.penup()
			f.color("pink")
			f.goto(x,y)
			blocks.append(f)
		
	time.sleep(delay)
	

# time.sleep(4)



# window.mainloop()
