import turtle
turtle.shape('turtle')
turtle.title('Lab 02')

# get the number of sides from user
n = int(turtle.textinput("Lab 02", "The number of sides: "))

# draw the n-side polygon using a for loop
# the length of a side is getting shorter as n getting larger
# When n = 4, the length of a side is 100.

for i in range(0, n):
    turtle.begin_fill()
    turtle.forward(360/n)
    turtle.right(60)
    turtle.end_fill()
    
turtle.penup()
# get the value of red color from user
r = float(turtle.textinput("Lab 02",
 "The red color component [between 0 and 1]: "))
# get the value of green color from user 
g = float(turtle.textinput("Lab 02",
 "The green color component [between 0 and 1]: "))
# get the value of blue color from user 
b = float(turtle.textinput("Lab 02",
 "The blue color component [between 0 and 1]: "))

#create the color from rgb values given by user
turtle.color(r,g,b)
#move the turtle to a new location below
turtle.goto(0, -200)
#draw a regular polygon with n sides and color(r,g,b)
#use a for loop
turtle.begin_fill()
for i in range(0, n):
    turtle.fillcolor(r,g,b)
    turtle.pendown()
    turtle.forward(360/n)
    turtle.right(60)
turtle.end_fill()
# make the turtle invisible
turtle.hideturtle()
#message for user
print("Please click on the graphics window to exit ...")
# wait for user to click on the screen to exit
#turtle…………………………………………………
turtle.exitonclick()