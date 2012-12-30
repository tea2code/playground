import time
import graphics.graphics
import physics.physics
from data import *
from tkinter import *

class Fun:
    loopTime = 1
    windowHeight = 480
    windowTitle = 'Fun with round things'
    windowWidth = 640

    def __init__( self ):
         # Initialize game data.
        self.data = data.Data()
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(20).setRadius(10).setColor('Green') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(120).setRadius(10).setColor('Blue') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(220).setRadius(10).setColor('Red') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(320).setRadius(10).setColor('Yellow') )

        # Create window and canvas.
        self.window = Tk()
        self.window.title( self.windowTitle )
        self.canvas = Canvas( self.window, width = self.windowWidth, height = self.windowHeight )
        self.canvas.pack()

        # Initialize physics.
        self.physics = physics.physics.Physics()

        # Initialize graphics.
        self.graphics = graphics.graphics.Graphics( self.canvas )
    
        # Initialize fps counter.
        self.lastTime = time.perf_counter()
        self.lastFrameTime = 0
        self.weightRatio = 0.7
        
        # Start.
        self.canvas.after( self.loopTime, self.__nextState )
        self.window.mainloop()
    
    def __nextState( self ):
        # Next state.
        self.physics.tick( self.data )
        self.graphics.tick( self.data )
        
        currentTime = time.perf_counter()
        frameTime = currentTime - self.lastTime
        fps = 1 / (frameTime * self.weightRatio + self.lastFrameTime * (1 - self.weightRatio))
        self.lastTime = currentTime
        self.lastFrameTime = frameTime
        self.window.title( self.windowTitle + ' ' + str(round(fps)) )
        
        self.canvas.after( self.loopTime, self.__nextState )
 
# Start application. 
Fun()