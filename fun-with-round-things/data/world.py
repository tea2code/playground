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
        ''' Test:
        >>> w = World()
        >>> w.height
        1
        >>> w.map
        >>> w.start.x == 0 and w.start.y == 0
        True
        >>> w.target.x == 0 and w.target.y == 0
        True
        >>> w.timelimit
        0
        >>> w.width
        1
        '''
        self.start = Vector2d.nullVector()
        self.target = Vector2d.nullVector()
        
    def __str__( self ):
        ''' Test:
        >>> w = World()
        >>> print(w)
        World(height 1.00, map None, start Vector2d(0.00, 0.00), target Vector2d(0.00, 0.00), timelimit 0.00, width 1.00)
        '''
        return 'World(height {0:.2f}, map {1}, start {2}, target {3}, timelimit {4:.2f}, width {5:.2f})'.format( self.height, self.map, self.start, self.target, self.timelimit, self.width )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()