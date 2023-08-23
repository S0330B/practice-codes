import turtle
from turtle import *


bgcolor("white")
color("black")


up()
goto(-80,200)
down()
fillcolor("black")
begin_fill()
forward(200)
setheading(270)
s=360

for i in range(9):
    s=s-10
    setheading(s)
    forward(10)
forward(180)
s=270

for i in range(9):
    s=s-10
    setheading(s)
    forward(10)
forward(200)
s=180

for i in range(9):
    s=s-10
    setheading(s)
    forward(10)
forward(180)
s=90


for i in range(9):
    s=s-10
    setheading(s)
    forward(10)
forward(30)
end_fill()

up()
color("white")
setheading(272)
forward(240)
setheading(0)
down()
color("#C60217")
fillcolor("#C60217")
begin_fill()
forward(30)
setheading(90)
forward(180)
setheading(180)
forward(30)
setheading(270)
forward(180)
end_fill()
setheading(0)
up()

forward(80)
down()
color("#C60217")
fillcolor("#C60217")
begin_fill()
forward(30)
setheading(90)
forward(180)
setheading(180)
forward(30)
setheading(270)
forward(180)
end_fill()

color("red")
fillcolor("red")
begin_fill()
setheading(114)
forward(197)
setheading(0)
forward(32)
setheading(293)
forward(196)
end_fill()
hideturtle()


up()
goto(-185,-220)
color("red")
write("NETFLIX",font=("Microsoft PhagsPa",80,"bold"))

turtle.done()