import random
from . import collider
from . import moveheun
from . import movestate
from . import reflector
from common.mathfunc import MathFunc
from common import tickable
from common import vector2d
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
        
        circle = data.circle
        
        # Move all circle.
        state = movestate.MoveState()
        state.force = circle.sumForces()
        circle.clearForces()
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
        collision = collider.Collider.collideCircleRect( circle.position.x, circle.position.y,
                                                         circle.radius, 0, rectHeight, rectWidth, 
                                                         rectX, rectY )
        if collision.isCollided: 
            data.collisions.append( collision )
            x, y = reflector.Reflector.reflectVector( circle.momentum.x, circle.momentum.y, 
                                                      border, 0, border, height )
            circle.momentum = vector2d.Vector2d( x, y )
        
        # Border top.
        rectHeight = border
        rectWidth = width
        rectX = width / 2
        rectY = border / 2
        collision = collider.Collider.collideCircleRect( circle.position.x, circle.position.y,
                                                         circle.radius, 0, rectHeight, rectWidth, 
                                                         rectX, rectY )
        if collision.isCollided: 
            data.collisions.append( collision )
            x, y = reflector.Reflector.reflectVector( circle.momentum.x, circle.momentum.y, 
                                                      0, border, width, border )
            circle.momentum = vector2d.Vector2d( x, y )
        
        # Border right.
        rectHeight = height
        rectWidth = border
        rectX = width - border / 2
        rectY = height / 2
        collision = collider.Collider.collideCircleRect( circle.position.x, circle.position.y,
                                                         circle.radius, 0, rectHeight, rectWidth, 
                                                         rectX, rectY )
        if collision.isCollided: 
            data.collisions.append( collision )
            x, y = reflector.Reflector.reflectVector( circle.momentum.x, circle.momentum.y, 
                                                      width - border, 0, width - border, height )
            circle.momentum = vector2d.Vector2d( x, y )
        
        # Border bottom.
        rectHeight = border
        rectWidth = width
        rectX = width / 2
        rectY = height - border / 2
        collision = collider.Collider.collideCircleRect( circle.position.x, circle.position.y,
                                                         circle.radius, 0, rectHeight, rectWidth, 
                                                         rectX, rectY )
        if collision.isCollided: 
            data.collisions.append( collision )
            x, y = reflector.Reflector.reflectVector( circle.momentum.x, circle.momentum.y, 
                                                      0, height - border, width, height - border )
            circle.momentum = vector2d.Vector2d( x, y )
        
        # Objects.
        for object in data.game.world.map.objects:
            if isinstance( object, datarect.Rect ):
                collision = collider.Collider.collideCircleRect( circle.position.x, circle.position.y,
                                                                 circle.radius, object.angle, object.height, 
                                                                 object.width, object.position.x, 
                                                                 object.position.y )
                if collision.isCollided: 
                    data.collisions.append( collision )
                    
                    # Calculate all four points of the rectangle without rotation.
                    heightHalf = object.height * 0.5
                    widthHalf = object.width * 0.5
                    xPlus = widthHalf
                    xMinus = -widthHalf
                    yPlus = heightHalf
                    yMinus = -heightHalf
                    
                    # Point 0.
                    x0 = xMinus
                    y0 = yMinus
                    
                    # Point 1.
                    x1 = xPlus
                    y1 = yMinus
                    
                    # Point 2.
                    x2 = xPlus
                    y2 = yPlus
                    
                    # Point 3.
                    x3 = xMinus
                    y3 = yPlus
                    
                    # Rotate collision point back.
                    cx = MathFunc.rotateX( collision.x - object.position.x, collision.y - object.position.y, -object.angle )
                    cy = MathFunc.rotateY( collision.x - object.position.x, collision.y - object.position.y, -object.angle )
                    
                    # Compare with points and calculate reflection.
                    epsilon = 0.00001
                    lx1 = 0
                    ly1 = 0
                    lx2 = 0
                    ly2 = 0
                    if self.__comparePoints( cx, cy, x0, y0 - epsilon, x1, y0 + epsilon ):
                        lx1 = MathFunc.rotateX( xMinus, yMinus, object.angle ) + object.position.x
                        ly1 = MathFunc.rotateY( xMinus, yMinus, object.angle ) + object.position.y
                        lx2 = MathFunc.rotateX( xPlus, yMinus, object.angle ) + object.position.x
                        ly2 = MathFunc.rotateY( xPlus, yMinus, object.angle ) + object.position.y
                    elif self.__comparePoints( cx, cy, x1 - epsilon, y1, x1 + epsilon, y2 ):
                        lx1 = MathFunc.rotateX( xPlus, yMinus, object.angle ) + object.position.x
                        ly1 = MathFunc.rotateY( xPlus, yMinus, object.angle ) + object.position.y
                        lx2 = MathFunc.rotateX( xPlus, yPlus, object.angle ) + object.position.x
                        ly2 = MathFunc.rotateY( xPlus, yPlus, object.angle ) + object.position.y
                    elif self.__comparePoints( cx, cy, x3, y3 - epsilon, x2, y3 + epsilon ):
                        lx1 = MathFunc.rotateX( xPlus, yPlus, object.angle ) + object.position.x
                        ly1 = MathFunc.rotateY( xPlus, yPlus, object.angle ) + object.position.y
                        lx2 = MathFunc.rotateX( xMinus, yPlus, object.angle ) + object.position.x
                        ly2 = MathFunc.rotateY( xMinus, yPlus, object.angle ) + object.position.y
                    elif self.__comparePoints( cx, cy, x0 - epsilon, y0, x0 + epsilon, y3 ):
                        lx1 = MathFunc.rotateX( xMinus, yPlus, object.angle ) + object.position.x
                        ly1 = MathFunc.rotateY( xMinus, yPlus, object.angle ) + object.position.y
                        lx2 = MathFunc.rotateX( xMinus, yMinus, object.angle ) + object.position.x
                        ly2 = MathFunc.rotateY( xMinus, yMinus, object.angle ) + object.position.y
                        
                    x, y = reflector.Reflector.reflectVector( circle.momentum.x, circle.momentum.y, 
                                                              lx1, ly1, lx2, ly2 )
                    circle.momentum = vector2d.Vector2d( x, y )
            else:
                raise TypeError( 'Unknown object "{0}" in map'.format(object) )
                    
    def __comparePoints( self, x0, y0, x1, y1, x2, y2 ):
        return x1 <= x0 and x0 <= x2 and y1 <= y0 and y0 <= y2