""" Class representing an 2d vector. """
class Vector2d:
    """ Constructor with the x and y component as parameters. """
    def __init__( self, x, y ):
        self.x = x
        self.y = y
        
    """ Static method to construct an null vector. """
    @staticmethod
    def nullVector():
        return Vector2d( 0, 0 )
        
    """ Add two vectors using + operator. Returns the resulting vector. """
    def __add__( self, other ):
        return Vector2d( self.x + other.x, self.y + other.y )
        
    """ Scalar multiplication using the * operator. Returns the resulting vector. """
    def __mul__( self, scalar ):
        return Vector2d( self.x * scalar, self.y * scalar )