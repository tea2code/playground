from common.vector2d import *

class MoveDerivative:
    """ Derivative class for integration of movable objects. 
    
    Member:
    force -- Force in the derivative of momentum.
    velocity -- Velocity is the derivative of position.
    """

    force = None
    velocity = None
    
    def __init__( self ):
        """ Test:
        >>> m = MoveDerivative()
        >>> m.force.x == 0 and m.force.y == 0
        True
        >>> m.velocity.x == 0 and m.velocity.y == 0
        True
        """
        self.force = Vector2d.nullVector()
        self.velocity = Vector2d.nullVector()
        
    def __str__( self ):
        """ Test:
        >>> m = MoveDerivative()
        >>> print(m)
        MoveDerivative(force Vector2d(0.00, 0.00), velocity Vector2d(0.00, 0.00))
        """
        return 'MoveDerivative(force {0}, velocity {1})'.format(self.force, self.velocity)
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()