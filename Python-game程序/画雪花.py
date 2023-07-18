#This program creates a snowflake with 6 arms. This takes you from the top of page 48 to step 8 on page 50.


from turtle import *

#set up the turtle
shape("turtle")
speed(10)
pencolor("white")
width(6)
#hideturtle

#set up the backdrop
Screen().bgcolor("turquoise")

#create a v shape to repeat
def vshape():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)


#use those Vs to create a single arm of a snowflake

def snowflakeArm():
    for x in range(0,4):
        forward(30)
        vshape()
    backward(120)
    
#function using a for loop to repeat snowflake arm x 18
def snowflake():
    for x in range(0,18):
        snowflakeArm()
        right(20)

snowflake()
