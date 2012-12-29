import data

from tkinter import *

def draw( canvas ):
    canvas.delete( ALL )
    canvas.configure( background = 'white' )
    
    for circle in data.circles:
        x = circle.posX
        y = circle.posY
        r = circle.radius
        c = circle.color
        canvas.create_oval( x - r, y - r, x + r, y + r, width = r, fill = c )