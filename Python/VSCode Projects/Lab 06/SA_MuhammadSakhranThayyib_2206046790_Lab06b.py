# lab06b.py
# This program draws a Hilbert curve fractal
import turtle as t
t.tracer(1, 0) # Increase the first argument to speed up the drawing. 
t.setworldcoordinates(0, 0, 700, 700)
t.color('blue')
t.hideturtle()

LINE_LENGTH = 8 # Try changing the line length by a litte. 
ANGLE = 90 # Try changing the turning angle by a few degrees.
LEVELS = 5 # Try changing the recursive

def hilbertCurveQuadrant(level, angle): 
    if level == 0:
# BASE CASE
        return
    else:
# level by a litte.
# RECURSIVE CASE
        t.right(angle)
        hilbertCurveQuadrant(level - 1, -angle)
        t.forward(LINE_LENGTH)
        t.left(angle)
        hilbertCurveQuadrant(level - 1, angle)
        t.forward(LINE_LENGTH)
        hilbertCurveQuadrant(level - 1, angle)
        t.left(angle)
        t.forward(LINE_LENGTH)
        hilbertCurveQuadrant(level - 1, -angle)
        t.right(angle)
    return


def hilbertCurve(startingPosition): # Move to starting position. 
    t.penup() 
    t.goto(startingPosition) 
    t.pendown()

hilbertCurveQuadrant(LEVELS, ANGLE) #Draw lower left quadrant
t.forward(LINE_LENGTH)

hilbertCurveQuadrant(LEVELS, ANGLE) #Draw Lower Right Quadrant
t.left(ANGLE)
t.forward(LINE_LENGTH)
t.left(ANGLE)

hilbertCurveQuadrant(LEVELS, ANGLE) # Draw upper right quadrant.
t.forward(LINE_LENGTH)

hilbertCurveQuadrant(LEVELS, ANGLE) # Draw upper left quadrant.
t.left(ANGLE)
t.forward(LINE_LENGTH)
t.left(ANGLE)

t.title()
t.title("A Hilbert Curve Fractal")
hilbertCurve((30, 350))
t.exitonclick()