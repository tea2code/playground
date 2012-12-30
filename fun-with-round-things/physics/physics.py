from data import data
import random

def execute():
    newCircles = []
    for circle in data.circles:
        circle.posX += randomInteger()
        #circle.posY += randomInteger()
        newCircles.append( circle )
    data.circles = newCircles

# Returns an integer between -5 and 5.
def randomInteger():
    # Create random integer and shift by 5.
    return round( random.random() * 10 ) - 5 