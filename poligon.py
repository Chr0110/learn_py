from turtle import *

def polygon(x, n, l):
    for i in range(n):
        x.fd(l)
        x.left(360 / n)
x = Turtle()
polygon(x, 200, 5)