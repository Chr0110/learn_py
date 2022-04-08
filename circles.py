import turtle
import time
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
    for coulours in ["red", "green", "yellow", "pink", "magenta","blue"]:
        turtle.color(coulours)
        turtle.circle(100)
        turtle.left(5)
time.sleep(2)
