import turtle
import random

t = turtle.Turtle()
#shortcut so that I don't write turtle

#chess time :O
turtle.screensize(3000,3000)
#sets the screensize

rows           = int(turtle.numinput("Colorful Chessboard and Flower Petals", "Insert the amount of rows and columns", \
    default=4, minval=1, maxval=100))
squareSize     = int(turtle.numinput("Colorful Chessboard and Flower Petals", "Insert the size of the squares", \
    default=1, minval=5, maxval=100))
petalNumber    = int(turtle.numinput("Colorful Chessboard and Flower Petals", "Insert the amount of petals", \
    default=6, minval=1, maxval=1000))
#inputs user values that is changed to variables

sizeNumberThing= squareSize*rows
numberofsquares= rows**2 
columns        = rows
#lists up very important variables for some very important codes and strings

t.speed(200)
#set the turtle speed
t.penup()
t.pendown()
#sets the pen up and down
for i in range(1, petalNumber+1):
    t.color(random.random(), random.random(), random.random())
    t.begin_fill()
    t.circle(60, 45)
    t.left(135)
    t.circle(60, 45)
    t.left(135)
    t.setheading(360*(i/petalNumber)) 
    t.end_fill()

#creates the petal via a loop

t.penup()
t.setpos(-(sizeNumberThing/2), -(100+sizeNumberThing)) #collabed with Muhammad Sean 
t.pendown()
#changes the turtle position so its below the flower

# rows = 5
# 


for i in range(rows):
    x = int()
    while x < rows:
            t.color(random.random(), random.random(), random.random())
            t.begin_fill()
            t.forward(squareSize)
            t.left(90)
            t.forward(squareSize)
            t.left(90)
            t.forward(squareSize)
            t.left(90)
            t.forward(squareSize)
            t.left(90)
            t.forward(squareSize)
            t.end_fill()
            x += 1
    t.penup()
    t.goto(-(sizeNumberThing/2), t.ycor()+squareSize) #collabed with Muhammad Oka, the OG
    t.pendown()
#draws the chessboard that is according to its wanted size and rows, modified to not overlap the flower no matter how big it is


turtle.penup()
turtle.goto(((-(sizeNumberThing/10))+15), -(sizeNumberThing+150))
#changes the turtle position to be below the chessboard 

turtle.down()
turtle.color('blue')
turtle.write(f"Colorful Chessboard of {numberofsquares} squares and Flower of {petalNumber} petals", \
    align='center', font=("Arial", 18, "normal"))
#writes the number of chessboard with its square quantity and the flower petal quantity

t.hideturtle()
turtle.hideturtle()
turtle.exitonclick()


