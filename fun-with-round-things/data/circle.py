from common.vector2d import *

class Circle:
    """ Class representing a circle. """

    color = 'black'
    position = None
    radius = 1
    velocity = None
    
    def __init__( self ):
        self.position = Vector2d.nullVector()
        self.velocity = Vector2d.nullVector()

    def setColor( self, color ):
        """ Sets the color and returns the object. """
        self.color = color
        return self
        
    def setPosition( self, position ):
        """ Sets the position (vector2d) and returns the object. """
        self.position = position
        return self
        
    def setPositionX( self, x ):
        """ Sets the x component of the position and returns the object. """
        self.position.x = x
        return self
    
    def setPositionY( self, y ):
        """ Sets the y component of the position and returns the object. """
        self.position.y = y
        return self
    
    def setRadius( self, radius ):
        """ Sets the radius and returns the object. """
        self.radius = radius
        return self
        
    def setVelocity( self, velocity ):
        """ Sets the velocity (vector2d) and returns the object. """
        self.velocity = velocity
        return self
        
    def __str__( self ):
        return 'Circle at (' + str(self.position.x) + ', ' + str(self.position.y) + ') with radius ' + str(self.radius) + ' and color "' + self.color + '".'