from common.mathfunc import MathFunc
from graphics import drawable

import math

class Rect( drawable.Drawable ):
    ''' Draws a rectangle. 
    
    Member:
    angle -- The angle in degree of the rectangle (int).
    height -- The height of the rectangle (int).
    width -- The width of the rectangle (int).
    x -- The x-component of the center of the rectangle (int).
    y -- The y-component of the center of the rectangle (int).
    '''
    angle = 0
    height = 1
    width = 1
    x = 0
    y = 0
    
    def __init__( self, angle, height, width, x, y ):
        ''' Initializes the rect.
        
        Test:
        >>> r = Rect( 1, 2, 3, 4, 5 )
        >>> r.angle
        1
        >>> r.height
        2
        >>> r.width
        3
        >>> r.x
        4
        >>> r.y
        5
        '''
        self.angle = angle
        self.height = height
        self.width = width
        self.x = x
        self.y = y
    
    def draw( self, canvas ):
        ''' Draws the rect on the given canvas. '''
        
        heightHalf = self.height * 0.5
        widthHalf = self.width * 0.5
        xPlus = widthHalf
        xMinus = -widthHalf
        yPlus = heightHalf
        yMinus = -heightHalf
        
        # Point 0.
        x0 = MathFunc.rotateX( xMinus, yMinus, self.angle ) + self.x
        y0 = MathFunc.rotateY( xMinus, yMinus, self.angle ) + self.y
        
        # Point 1.
        x1 = MathFunc.rotateX( xPlus, yMinus, self.angle ) + self.x
        y1 = MathFunc.rotateY( xPlus, yMinus, self.angle ) + self.y
        
        # Point 2.
        x2 = MathFunc.rotateX( xPlus, yPlus, self.angle ) + self.x
        y2 = MathFunc.rotateY( xPlus, yPlus, self.angle ) + self.y
        
        # Point 3.
        x3 = MathFunc.rotateX( xMinus, yPlus, self.angle ) + self.x
        y3 = MathFunc.rotateY( xMinus, yPlus, self.angle ) + self.y
        
        # Draw.
        canvas.create_polygon( x0, y0, x1, y1, x2, y2, x3, y3, fill = '', outline = 'black' )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()