#This program creates a snowflake with six arms. Each arm is a randomly-generated colour.


from turtle import *
#this is a new line
import random


shape("turtle")
speed(10)
#this is where color originally went in the version of the program on pages 48-50
width(6)

sky = Screen()
sky.bgcolor("turquoise")

colours = ["blue", "purple", "cyan", "white", "yellow", "green", "orange"]


def vshape():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)

def snowflakeArm():
    for x in range(0,4):
        forward(30)
        vshape()
    backward(120)


def snowflake():
    for x in range(0,6):
        color(random.choice(colours))
        snowflakeArm()
        right(60)
        
snowflake()
