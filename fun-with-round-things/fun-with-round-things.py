import fps.fps
import gamerules.gamerules
import graphics.tkgraphics
import physics.physics

from common.timestepper import *
from common.vector2d import *
from data import *
from gamerules.gamestarter import *

class Fun:
    ''' Main class.

    Member:
    data -- The "global" data object.
    fps -- The frames per second counter.
    frameTime -- "Should be" time of one frame.
    gameRules -- The module responsible for game rules.
    graphics -- The module responsible for visualizing the data.
    loopTime -- The overall refreshing time of the main loop. 
    physics -- The module responsible for physics.
    timestepper -- The frame ticker.
    windowTitle -- The window title.
    '''
    data = None
    fps = None
    frameTime = 1/60
    gameRules = None
    graphics = None
    loopTime = 1
    physics = None
    timestepper = None
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
        ''' Start the application. '''
        # Start.
        self.timestepper.start()
        self.__callNextState()
        self.graphics.window.mainloop()
    
    def calculateNextState( self, t, dt ):
        ''' Callback function for the frame ticker. Executes all modules on the data. '''
        self.data.deltaTime = dt
        self.data.time = t
        self.physics.tick( self.data )
        self.gameRules.tick( self.data )
        self.graphics.tick( self.data )
        self.fps.tick( self.data ) 
    
    def __callNextState( self ):
        ''' Return to main loop. '''
        self.graphics.canvas.after( self.loopTime, self.__nextState )
    
    def __nextState( self ):
        ''' Callback function for the main loop. '''
        self.timestepper.tick()    
        self.__callNextState()
        
# Start application. 
if __name__ == '__main__':
    Fun().begin()