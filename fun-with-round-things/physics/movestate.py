from common.vector2d import *

class MoveState:
    """ State class for integration of movable objects. 
    
    Member:
    force -- Force in the derivative of momentum.
    mass -- The mass (float).
    momentum -- The momentum (Vector2d).
    position -- The position (Vector2d).
    """
    
    force = None
    mass = 0
    momentum = None
    position = None
    
    def __init__( self ):
        """ Test:
        >>> m = MoveState()
        >>> m.force.x == 0 and m.force.y == 0
        True
        >>> m.mass
        0
        >>> m.position.x == 0 and m.position.y == 0
        True
        >>> m.momentum.x == 0 and m.momentum.y == 0
        True
        """
        self.force = Vector2d.nullVector()
        self.momentum = Vector2d.nullVector()
        self.position = Vector2d.nullVector()

    def velocity( self ):
        """ Calculates the current velocity and returns it (Vector2d).
            
        Test:
        >>> m = MoveState()
        >>> m.mass = 2
        >>> m.momentum = Vector2d(10, 6)
        >>> v = m.velocity()
        >>> round(v.x)
        5
        >>> round(v.y)
        3
        """
        return self.momentum * (1/self.mass)
        
    def __str__( self ):
        """ Test:
        >>> m = MoveState()
        >>> print(m)
        MoveState(force Vector2d(0.00, 0.00), mass 0.00, momentum Vector2d(0.00, 0.00), position Vector2d(0.00, 0.00))
        """
        return 'MoveState(force {0}, mass {1:.2f}, momentum {2}, position {3})'.format(self.force, self.mass, self.momentum, self.position)
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()