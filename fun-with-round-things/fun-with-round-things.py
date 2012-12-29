import circle
import data
import graphics
import physics

from tkinter import *

root = Tk()
root.title( 'Fun with round things' )
canvas = Canvas( root, width = 500, height = 400 )
canvas.pack()
td = 16

data.circles.append( circle.Circle(200, 20, 10) )
data.circles.append( circle.Circle(200, 120, 10) )
data.circles.append( circle.Circle(200, 220, 10) )
data.circles.append( circle.Circle(200, 320, 10) )

def loop():
    global canvas, counter, td

    physics.execute()
    graphics.draw( canvas )
    canvas.after( td, loop )

canvas.after( td, loop )
root.mainloop()