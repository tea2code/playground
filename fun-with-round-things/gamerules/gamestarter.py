from data.circle import *
from map.maploader import *

class GameStarter:
    ''' Loads und initializes a game. 
    
    Member:
    _data -- The data object.
    '''
    _data = None
    
    def __init__( self, data ):
        ''' Parameter:
        data -- The data object.
        
        Test:
        >>> from data.data import *
        >>> g = GameStarter( Data() )
        >>> g._data # doctest: +ELLIPSIS
        <...Data object at 0x...>
        '''
        self._data = data
        
    def load( self, mapFile ):
        ''' Loads the map and initializes the game data. After this method call the game is ready 
        to start.

        Parameter:
        mapFile -- The path to the map. '''
        mapLoader = MapLoader()
        self._data.game = mapLoader.load( mapFile )
        self._data.target = self._data.game.world.target
        self._data.timeLimit = self._data.game.world.timelimit
        self._data.windowHeight = self._data.game.world.height
        self._data.windowWidth = self._data.game.world.width
        
        self._data.acceleration = 14 # Pixel per second^2
        
        c = Circle()
        c.setPosition( self._data.game.world.start )
        c.setRadius( 10 )
        c.setColor( 'Green' )
        c.setMass( 1 )
        c.addForce( Vector2d(self._data.acceleration, 0) )
        self._data.circles.append( c )