import fps.fps
import graphics.tkgraphics
import physics.physics
from common.timestepper import *
from common.vector2d import *
from data import *

class Fun:
    frameTime = 1/60
    loopTime = 1
    windowHeight = 480
    windowTitle = 'Fun with round things'
    windowWidth = 640

    def __init__( self ):
        # Initialize game data.
        self.data = data.Data()
        self.data.acceleration = 14 # Pixel per second^2
        self.data.circles.append( circle.Circle().setPositionX(20).setPositionY(100).setRadius(10).setColor('Green').setMass(1).addForce(Vector2d(14, 0)) )
        self.data.target = Vector2d( 720, 100 )
        self.data.timeLimit = 10
        self.data.windowHeight = 200
        self.data.windowTitle = 'Fun with round things'
        self.data.windowWidth = 800

        # Initialize physics.
        self.physics = physics.physics.Physics()

        # Initialize graphics.
        self.graphics = graphics.tkgraphics.TkGraphics( self.data )
    
        # Initialize fps counter.
        self.fps = fps.fps.Fps( 60, 120 )
        
        # Initialize time stepper.
        self.timestepper = Timestepper( self.frameTime, self.calculateNextState )
        self.timestepper.time = self.frameTime
        
    def begin( self ):
        # Start.
        self.timestepper.start()
        self.__callNextState()
        self.graphics.window.mainloop()
    
    def calculateNextState( self, t, dt ):
        self.data.deltaTime = dt
        self.data.time = t
        self.physics.tick( self.data )
        self.graphics.tick( self.data )
        self.fps.tick( self.data ) 
    
    def __callNextState( self ):
        self.graphics.canvas.after( self.loopTime, self.__nextState )
    
    def __nextState( self ):
        self.timestepper.tick()    
        self.__callNextState()
        
# Start application. 
if __name__ == '__main__':
    Fun().begin()