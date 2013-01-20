import fps.fps
import gamerules.gamerules
import graphics.tkgraphics
import physics.physics

from common.timestepper import *
from common.vector2d import *
from data import *
from gamerules.gamestarter import *

class Fun:
    frameTime = 1/60
    loopTime = 1
    windowTitle = 'Fun with round things'

    def __init__( self ):
        # Initialize game data.
        self.data = data.Data()
        gameStarter = GameStarter( self.data )
        gameStarter.load( 'maps/Integration Test.xml' )
        self.data.windowTitle = self.windowTitle

        # Initialize physics.
        self.physics = physics.physics.Physics()
        
        # Initialize game rules.
        self.gameRules = gamerules.gamerules.GameRules()

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
        self.gameRules.tick( self.data )
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