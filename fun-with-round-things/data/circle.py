from . import movable
from common.vector2d import *

class Circle( movable.Movable ):
    ''' Class representing a circle. 
    
    Member:
    color -- Color of the circle.
    radius -- Radius of the circle.
    '''

    color = 'black'
    radius = 1
    
    def __init__( self ):
        ''' Test:
        >>> c = Circle()
        >>> c.color
        'black'
        >>> c.radius
        1
        '''
        super().__init__()
    
    def setColor( self, color ):
        ''' Sets the color and returns the object. 
        
        Test:
        >>> c = Circle()
        >>> c.color
        'black'
        >>> c.setColor( 'white' ).color
        'white'
        '''
        self.color = color
        return self
        
    def setRadius( self, radius ):
        ''' Sets the radius and returns the object. 
        
        Test:
        >>> c = Circle()
        >>> c.radius
        1
        >>> c.setRadius( 2 ).radius
        2
        '''
        self.radius = radius
        return self
        
    def __str__( self ):
        ''' Test:
        >>> c = Circle()
        >>> print(c)
        Circle(color black, radius 1.00, Movable(forces [], mass 0.00, momentum Vector2d(0.00, 0.00), position Vector2d(0.00, 0.00)))
        '''
        return 'Circle(color {0}, radius {1:.2f}, {2})'.format( self.color, self.radius, 
                                                                super().__str__() )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()