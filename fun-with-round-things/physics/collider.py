from . import collision
from common import mathfunc

import math

class Collider:
    ''' Collects functions which are collision detection related. '''
    
    @staticmethod
    def collideCircleRect( circleX, circleY, circleRadius, rectAngle, rectHeight, rectWidth, rectX, rectY ):
        ''' Calculates collision between a circle and a rect. Returns the resulting collision object.
        
        Parameter:
        circleX -- The x-coordinate of the circle center.
        circleY -- The y-coordinate of the circle center.
        circleRadius -- The circle radius.
        rectAngle -- The angle of the rect.
        rectHeight -- The height of the rect.
        rectWidth -- The width of the rect.
        rectX - The x-coordinate of the rect center.
        rectY - The y-coordinate of the rect center.
        
        Test:
        >>> Collider.collideCircleRect(-100, -100, 10, 10, 10, 10, 100, 100).isCollided
        False
        >>> collision = Collider.collideCircleRect(10, 10, 5, -45, 10, 4.2, 14.95, 5.05)
        >>> collision.isCollided
        True
        >>> print( '{0:.2f}'.format(collision.x) )
        13.47
        >>> print( '{0:.2f}'.format(collision.y) )
        6.53
        '''
        # Keep rectangle static and rotate circle according to angle.
        radianAngle = math.radians( -rectAngle )
        cos = math.cos(radianAngle)
        sin = math.sin(radianAngle)
        distX = circleX - rectX
        distY = circleY - rectY
        cx = cos * distX - sin * distY + rectX
        cy = sin * distX + cos * distY + rectY
        
        # Closest point.
        x = 0
        y = 0
        
        # Find the closest x-coordinate from center of circle.
        rectWidthHalf = rectWidth * 0.5
        if cx < rectX - rectWidthHalf:
            x = rectX - rectWidthHalf
        elif cx > rectX + rectWidthHalf:
            x = rectX + rectWidthHalf
        else:
            x = cx
            
        # Find the closest y-coordinate from center of circle.
        rectHeightHalf = rectHeight * 0.5
        if cy < rectY - rectHeightHalf:
            y = rectY - rectHeightHalf
        elif cy > rectY + rectHeightHalf:
            y = rectY + rectHeightHalf
        else:
            y = cy
            
        # Determine collision.
        isCollided = False
        distance = mathfunc.MathFunc.euclideanDistance( cx, cy, x, y )
        if distance < circleRadius:
            isCollided = True
        
        # Rotate result point back.
        radianAngle = math.radians( rectAngle )
        cos = math.cos(radianAngle)
        sin = math.sin(radianAngle)
        distX = x - rectX
        distY = y - rectY
        x = cos * distX - sin * distY + rectX
        y = sin * distX + cos * distY + rectY

        # Result.
        c = collision.Collision( isCollided )
        c.x = x
        c.y = y
        return c
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()