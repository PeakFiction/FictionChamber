## Author: Muhammad Sakhran Thayyib AKA Duden
## File Name: lab02b.py
## prompt user for the number of sides and the color component (r,g,b)

import turtle

turtle.shape('turtle')
turtle.title('Lab 02')

# get the number of sides from the user
n = int(turtle.textinput("Lab 02", "The number of sides: "))

# draw the n-side polygon using a for loop
# the length of a side is getting shorter as n getting longer
# when n = 4, the length of a side is 100

for element in range(0, n):
    turtle.forward(360/n)
    turtle.right(60)

turtle.penup()
#takes the pen up as to not draw anything during travel

turtle.goto(0, -150)
#goes below the original hexa for better positioning

#get the value of the colour from the user"

redrgb = float(turtle.textinput("Insert Red RGB Value", "Between 0 and 1"))
#asks for the red rgb value to the user
greenrgb = float(turtle.textinput("Insert Green RGB Value", "Between 0 and 1"))
#asks for the green rgb value to the user
bluergb = float(turtle.textinput("Insert Blue RGB Value", "Between 0 and 1"))
#asks for the blue rgb value to the user

turtle.pendown()
#puts the pen down for drawing
turtle.begin_fill()
#tells the turtle to begin filling the figure
for element in range(0,n):
    turtle.color(redrgb, greenrgb, bluergb)
    turtle.forward(360/n)
    turtle.right(60)
turtle.end_fill()
#for l

turtle.penup()
turtle.goto (-200,100)


turtle.color("black")
turtle.write("Please click on the graphics window to exit", font=("Chiller", 20, "normal"))
turtle.hideturtle()
#message for user

print("Please click on the graphics window to exit")

turtle.exitonclick()


