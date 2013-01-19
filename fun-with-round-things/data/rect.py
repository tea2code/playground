from common.vector2d import *

class Rect:
    ''' A non-movable rect object. 
    
    Member:
    angle -- The angle in degree of the rect (int).
    height -- The height of the rect (int).
    position -- The position/center of the rect (Vector2d).
    width -- The width of the rect (int).
    '''
    angle = 0
    height = 1
    position = None
    width = 1
    
    def __init__( self ):
        ''' Test: 
        >>> r = Rect()
        >>> r.angle
        0
        >>> r.height
        1
        >>> r.position.x == 0 and r.position.y == 0
        True
        >>> r.width
        1
        '''
        self.position = Vector2d.nullVector()
        
    def __str__( self ):
        ''' Test:
        >>> r = Rect()
        >>> print( r )
        Rect(angle 0.00, height 1.00, position Vector2d(0.00, 0.00), width 1.00)
        '''
        return 'Rect(angle {0:.2f}, height {1:.2f}, position {2}, width {3:.2f})'.format(self.angle, self.height, self.position, self.width)
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()