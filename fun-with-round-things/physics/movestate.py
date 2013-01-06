class MoveState:
    """ State class for integration of movable objects. """
    
    x = 0
    v = 0

    def __add__( self, other ):
        """ Sum up two move states using +. Corresponds to addition of vectors.
        
        Test:
        >>> m1 = MoveState()
        >>> m1.x = 1
        >>> m1.v = 2
        >>> m2 = MoveState()
        >>> m2.x = 3
        >>> m2.v = 4
        >>> print(m1 + m2)
        MoveState(x 4.00, v 6.00)
        """
        new = MoveState()
        new.x = self.x + other.x
        new.v = self.v + other.v
        return new
    
    def __mul__( self, scalar ):
        """ Multiplicate object with scalar using *. Corresponds to scalar multiplication of vectors.
        
        Test:
        >>> m = MoveState()
        >>> m.x = 1
        >>> m.v = 2
        >>> print(m * 5)
        MoveState(x 5.00, v 10.00)
        """
        new = MoveState()
        new.x = self.x * scalar
        new.v = self.v * scalar
        return new
        
    def __str__( self ):
        """ Test:
        >>> m = MoveState()
        >>> print(m)
        MoveState(x 0.00, v 0.00)
        """
        return 'MoveState(x {:.2f}, v {:.2f})'.format(self.x, self.v)
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()