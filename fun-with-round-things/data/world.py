from common.vector2d import *

class World:
    ''' This represents the world aka a collection of maps of a game. 
    
    Member:
    height -- The height of the map (int).
    map -- The map.
    start -- Start point (Vector2d).
    target -- Target point (Vector2d).
    timelimit -- Time limit in seconds for this map (int)
    width -- The width of the map (int).
    '''
    height = 1
    map = None
    start = None
    target = None
    timelimit = 0
    width = 1
    
    def __init__( self ):
        start = Vector2d.nullVector()
        start = Vector2d.nullVector()