import turtle

turtle.color('red')

# Balls 1
turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
turtle.circle(50)
turtle.penup()

# Balls 2
turtle.goto(50, 0)
turtle.pendown()
turtle.circle(50)
turtle.penup()

# Shlong
turtle.goto(-25, 90)
turtle.left(90)
turtle.pendown()
turtle.forward(200)
turtle.right(180)
turtle.circle(25)
turtle.penup()
turtle.goto(25,290)
turtle.pendown()
turtle.forward(200)

turtle.hideturtle()
turtle.exitonclick()