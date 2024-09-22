#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(gaeo, sides):
   for s in range(sides):
       gaeo.forward(50)
       gaeo.right(360/sides)

def fillCorner(maya, corner):
    #draw big square
    drawSquare(maya, 100)
    
    if corner == 1:
        maya.begin_fill()
        drawSquare(maya, 50)
        maya.end_fill()
    elif corner == 2:
        maya.forward(50)
        maya.begin_fill()
        drawSquare(maya, 50)
        maya.end_fill()
    if corner == 3:
        maya.backward(100)
        maya.begin_fill()
        drawSquare(maya, 50)
        maya.end_fill()

def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle, 10)

    fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
