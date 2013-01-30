import random
from . import collider
from . import moveheun
from . import movestate
from common import tickable
from data import rect as datarect

class Physics( tickable.Tickable ):
    ''' This class calculates the physical reactions of all objects. '''

    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Calculates the physic on all objects. '''

        del data.collisions[:]
        
        border = data.game.world.map.border
        height = data.game.world.height
        width = data.game.world.width
        lhc = collider.Collider() # Let's smash particles and create scary black holes.
        
        for circle in data.circles:
            # Move all circles.
            state = movestate.MoveState()
            state.force = circle.sumForces()
            state.mass = circle.mass
            state.momentum = circle.momentum
            state.position = circle.position

            newState = moveheun.MoveHeun.integrate( state, data.deltaTime )
            circle.momentum = newState.momentum
            circle.position = newState.position
            
            # Check for collisions.            
            # Border left.
            rectHeight = height
            rectWidth = border
            rectX = border / 2
            rectY = height / 2
            collision = lhc.collideCircleRect( circle.position.x, circle.position.y,
                                               circle.radius, 0, rectHeight, rectWidth, 
                                               rectX, rectY )
            if collision.isCollided: 
                data.collisions.append( collision )
                circle.stop()
            
            # Border top.
            rectHeight = border
            rectWidth = width
            rectX = width / 2
            rectY = border / 2
            collision = lhc.collideCircleRect( circle.position.x, circle.position.y,
                                               circle.radius, 0, rectHeight, rectWidth, 
                                               rectX, rectY )
            if collision.isCollided: 
                data.collisions.append( collision )
                circle.stop()
            
            # Border right.
            rectHeight = height
            rectWidth = border
            rectX = width - border / 2
            rectY = height / 2
            collision = lhc.collideCircleRect( circle.position.x, circle.position.y,
                                               circle.radius, 0, rectHeight, rectWidth, 
                                               rectX, rectY )
            if collision.isCollided: 
                data.collisions.append( collision )
                circle.stop()
            
            # Border bottom.
            rectHeight = border
            rectWidth = width
            rectX = width / 2
            rectY = height - border / 2
            collision = lhc.collideCircleRect( circle.position.x, circle.position.y,
                                               circle.radius, 0, rectHeight, rectWidth, 
                                               rectX, rectY )
            if collision.isCollided: 
                data.collisions.append( collision )
                circle.stop()
            
            # Objects.
            for object in data.game.world.map.objects:
                if isinstance( object, datarect.Rect ):
                    collision = lhc.collideCircleRect( circle.position.x, circle.position.y,
                                                       circle.radius, object.angle, object.height, 
                                                       object.width, object.position.x, 
                                                       object.position.y )
                    if collision.isCollided: 
                        data.collisions.append( collision )
                        circle.stop()
                else:
                    raise TypeError( 'Unknown object "{0}" in map'.format(object) )