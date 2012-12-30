from common import vector2d

""" Class representing a circle. """
class Circle:
    color = 'black'
    position = vector2d.Vector2d.nullVector()
    radius = 1

    """ Sets the color and returns the object. """
    def setColor( self, color ):
        self.color = color
        return self
        
    """ Sets the position (vector2d) and returns the object. """
    def setPosition( self, position ):
        self.position = position
        return self
        
    """ Sets the x component of the position and returns the object. """
    def setPositionX( self, x ):
        self.position.x = x
        return self
    
    """ Sets the y component of the position and returns the object. """
    def setPositionY( self, y ):
        self.position.y = y
        return self
    
    """ Sets the radius and returns the object. """
    def setRadius( self, radius ):
        self.radius = radius
        return self