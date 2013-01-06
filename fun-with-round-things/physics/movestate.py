class MoveState:
    """ State class for integration of movable objects. 
    
    Member:
    position -- The position.
    velocity -- The velocity.
    """
    
    position = 0
    velocity = 0

    def __add__( self, other ):
        """ Sum up two move states using +. Corresponds to addition of vectors.
        
        Test:
        >>> m1 = MoveState()
        >>> m1.position = 1
        >>> m1.velocity = 2
        >>> m2 = MoveState()
        >>> m2.position = 3
        >>> m2.velocity = 4
        >>> print(m1 + m2)
        MoveState(position 4.00, velocity 6.00)
        """
        new = MoveState()
        new.position = self.position + other.position
        new.velocity = self.velocity + other.velocity
        return new
    
    def __mul__( self, scalar ):
        """ Multiplicate object with scalar using *. Corresponds to scalar multiplication of vectors.
        
        Test:
        >>> m = MoveState()
        >>> m.position = 1
        >>> m.velocity = 2
        >>> print(m * 5)
        MoveState(position 5.00, velocity 10.00)
        """
        new = MoveState()
        new.position = self.position * scalar
        new.velocity = self.velocity * scalar
        return new
        
    def __str__( self ):
        """ Test:
        >>> m = MoveState()
        >>> print(m)
        MoveState(position 0.00, velocity 0.00)
        """
        return 'MoveState(position {:.2f}, velocity {:.2f})'.format(self.position, self.velocity)
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()