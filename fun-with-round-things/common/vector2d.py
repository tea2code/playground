class Vector2d:
    """ Class representing an 2d vector. 
    
    Member:
    x - The x component.
    y - The y component.
    """
    
    x = 0
    y = 0
    
    def __init__( self, x, y ):
        """ Constructor with the x and y component as parameters. """
        self.x = x
        self.y = y
        
    @staticmethod
    def nullVector():
        """ Static method to construct an null vector. 
        
        Test:
        >>> v = Vector2d.nullVector()
        >>> v.x
        0
        >>> v.y
        0
        """
        return Vector2d( 0, 0 )
        
    def __add__( self, other ):
        """ Add two vectors using + operator. Returns the resulting vector. 
        
        Test:
        >>> v1 = Vector2d(1, 2)
        >>> v2 = Vector2d(3, 4)
        >>> v3 = v1 + v2
        >>> v3.x
        4
        >>> v3.y
        6
        """
        return Vector2d( self.x + other.x, self.y + other.y )
        
    def __mul__( self, scalar ):
        """ Scalar multiplication using the * operator. Returns the resulting vector. 
        
        Test:
        >>> v1 = Vector2d(1, 2)
        >>> v2 = v1 * 5
        >>> v2.x
        5
        >>> v2.y
        10
        """
        return Vector2d( self.x * scalar, self.y * scalar )
        
    def __str__( self ):
        return 'Vector2d({:.2f}, {:.2f})'.format(self.x, self.y)
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()