from data import circle
from data import data
from graphics import graphics
from physics import physics
import time

from tkinter import *

root = Tk()
root.title( 'Fun with round things' )
canvas = Canvas( root, width = 500, height = 400 )
canvas.pack()
td = 1

data.circles.append( circle.Circle(200, 20, 10) )
data.circles.append( circle.Circle(200, 120, 10) )
data.circles.append( circle.Circle(200, 220, 10) )
data.circles.append( circle.Circle(200, 320, 10) )

lastTime = time.perf_counter()
lastFrameTime = 0
weightRatio = 0.7
    
def loop():
    global canvas, counter, td, lastFrameTime, weightRatio, lastTime

    physics.execute()
    graphics.draw( canvas )
    canvas.after( td, loop )
    
    currentTime = time.perf_counter()
    frameTime = currentTime - lastTime
    fps = 1 / (frameTime * weightRatio + lastFrameTime * (1 - weightRatio))
    lastTime = currentTime
    lastFrameTime = frameTime
    print( fps )

canvas.after( td, loop )
root.mainloop()