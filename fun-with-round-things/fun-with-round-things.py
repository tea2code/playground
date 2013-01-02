import fps.fps
import time
import graphics.tkgraphics
import physics.physics
from data import *

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
        self.data.windowHeight = 480
        self.data.windowTitle = 'Fun with round things'
        self.data.windowWidth = 640

        # Initialize physics.
        self.physics = physics.physics.Physics()

        # Initialize graphics.
        self.graphics = graphics.tkgraphics.TkGraphics( self.data )
    
        # Initialize fps counter.
        self.fps = fps.fps.Fps( 500, 1000 )
        
    def begin( self ):
        # Start.
        self.graphics.canvas.after( self.loopTime, self.__nextState )
        self.graphics.window.mainloop()
    
    def __nextState( self ):
        # Next state.
        self.physics.tick( self.data )
        self.graphics.tick( self.data )
        self.fps.tick( self.data ) 
        
        self.graphics.canvas.after( self.loopTime, self.__nextState )

# Start application. 
if __name__ == '__main__':
    Fun().begin()