from common import vector2d
from data import circle
from map import maploader

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
        mapLoader = maploader.MapLoader()
        self._data.game = mapLoader.load( mapFile )

        c = circle.Circle()
        c.setPosition( self._data.game.world.start )
        c.setRadius( 10 )
        c.setColor( 'Green' )
        c.setMass( 1 )
        self._data.circle = c