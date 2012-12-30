class Vector2d:
    """ Class representing an 2d vector. """
    
    def __init__( self, x, y ):
        """ Constructor with the x and y component as parameters. """
        self.x = x
        self.y = y
        
    @staticmethod
    def nullVector():
        """ Static method to construct an null vector. """
        return Vector2d( 0, 0 )
        
    def __add__( self, other ):
        """ Add two vectors using + operator. Returns the resulting vector. """
        return Vector2d( self.x + other.x, self.y + other.y )
        
    def __mul__( self, scalar ):
        """ Scalar multiplication using the * operator. Returns the resulting vector. """
        return Vector2d( self.x * scalar, self.y * scalar )