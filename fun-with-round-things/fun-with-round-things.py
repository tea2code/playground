import fpscounter
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
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(420).setRadius(10).setColor('Violet') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(20).setRadius(10).setColor('Green') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(120).setRadius(10).setColor('Blue') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(220).setRadius(10).setColor('Red') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(320).setRadius(10).setColor('Yellow') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(420).setRadius(10).setColor('Violet') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(20).setRadius(10).setColor('Green') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(120).setRadius(10).setColor('Blue') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(220).setRadius(10).setColor('Red') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(320).setRadius(10).setColor('Yellow') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(420).setRadius(10).setColor('Violet') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(20).setRadius(10).setColor('Green') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(120).setRadius(10).setColor('Blue') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(220).setRadius(10).setColor('Red') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(320).setRadius(10).setColor('Yellow') )
        self.data.circles.append( circle.Circle().setPositionX(200).setPositionY(420).setRadius(10).setColor('Violet') )

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
        self.frameCounter = 0
        self.maxFrameCounts = 300
        self.fpsCounter = fpscounter.FpsCounter( 1000 )
        
    def begin( self ):
        # Start.
        self.fpsCounter.start()
        self.canvas.after( self.loopTime, self.__nextState )
        self.window.mainloop()
    
    def __nextState( self ):
        # Next state.
        self.physics.tick( self.data )
        self.graphics.tick( self.data )
        
        self.fpsCounter.tick()
        self.frameCounter += 1
        if self.frameCounter > self.maxFrameCounts:
            fps = round( self.fpsCounter.fps() )
            self.window.title( self.windowTitle + ' (' + str(fps) + ' fps)' )
            self.frameCounter = 0
        
        self.canvas.after( self.loopTime, self.__nextState )

# Start application. 
if __name__ == '__main__':
    Fun().begin()