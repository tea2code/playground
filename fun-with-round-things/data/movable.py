from abc import ABCMeta
from common.vector2d import *

class Movable(metaclass = ABCMeta):
    """ This abstract class represents a movable object. 
    
    Members:
    forces -- List of force vectors (Vector2d).
    mass -- The mass of the object (float).
    position -- The position of the object (Vector2d).
    velocity -- The velocity of the object (Vector2d).
    """
    
    forces = []
    mass = 0
    position = None
    velocity = None
    
    def __init__( self ):
        """ Test:
        >>> m = Movable()
        >>> m.forces
        []
        >>> m.mass
        0
        >>> m.position.x == 0 and m.position.y == 0
        True
        >>> m.velocity.x == 0 and m.velocity.y == 0
        True
        """
        self.position = Vector2d.nullVector()
        self.velocity = Vector2d.nullVector()
    
    def addForce( self, force ):
        """ Adds force to object (Vector2d). Returns this.

        Test:
        >>> m = Movable()
        >>> m.addForce( Vector2d(1, 2) ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m.forces[0].x == 1 and m.forces[0].y == 2
        True
        """
        self.forces.append( force )
        return self
        
    def clearForces( self ):
        """ Removes all forces. Returns this. 

        Test:
        >>> m = Movable()
        >>> m.addForce( Vector2d(1, 2) ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> len(m.clearForces().forces) == 0
        True
        """
        del self.forces[:]
        return self
        
    def setMass( self, mass ):
        """ Sets mass (float). Returns this. 
        
        Test:
        >>> m = Movable()
        >>> m.setMass( 1 ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m.mass
        1
        """
        self.mass = mass
        return self
        
    def setPosition( self, position ):
        """ Sets the position (Vector2d). Returns this. 
        
        Test:
        >>> m = Movable()
        >>> m.setPosition( Vector2d(2, 3) ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m.position.x == 2 and m.position.y == 3
        True
        """
        self.position = position
        return self
        
    def setPositionX( self, x ):
        """ Sets the x component of the position. Returns this. 
        
        Test:
        >>> m = Movable()
        >>> m.setPositionX( 2 ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m.position.x == 2 and m.position.y == 0
        True
        """
        self.position.x = x
        return self
    
    def setPositionY( self, y ):
        """ Sets the y component of the position. Returns this. 
        
        Test:
        >>> m = Movable()
        >>> m.setPositionY( 2 ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m.position.x == 0 and m.position.y == 2
        True
        """
        self.position.y = y
        return self
        
    def setVelocity( self, velocity ):
        """ Sets the velocity (Vector2d). Returns this. 
        
        Test:
        >>> m = Movable()
        >>> m.setVelocity( Vector2d(2, 3) ) # doctest: +ELLIPSIS
        <...Movable object at 0x...>
        >>> m.velocity.x == 2 and m.velocity.y == 3
        True
        """
        self.velocity = velocity
        return self
        
    def __str__( self ):
        """ Test:
        >>> m = Movable()
        >>> print(m)
        Movable(forces [], mass 0.00, position Vector2d(0.00, 0.00), velocity Vector2d(0.00, 0.00))
        """
        forces = ", ".join( [str(element) for element in self.forces]  )
        return 'Movable(forces [{0}], mass {1:.2f}, position {2}, velocity {3})'.format(forces, self.mass, self.position, self.velocity)
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()