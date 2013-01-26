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
        
        radianAngle = math.radians( self.angle )
        cosAngle = math.cos( radianAngle )
        sinAngle = math.sin( radianAngle )
        heightHalf = self.height / 2
        widthHalf = self.width / 2
        xPlus = widthHalf
        xMinus = -widthHalf
        yPlus = heightHalf
        yMinus = -heightHalf
        
        # Point 0.
        x0 = self.__transformX( xMinus, yMinus, cosAngle, sinAngle ) + self.x
        y0 = self.__transformY( xMinus, yMinus, cosAngle, sinAngle ) + self.y
        
        # Point 1.
        x1 = self.__transformX( xPlus, yMinus, cosAngle, sinAngle ) + self.x
        y1 = self.__transformY( xPlus, yMinus, cosAngle, sinAngle ) + self.y
        
        # Point 2.
        x2 = self.__transformX( xPlus, yPlus, cosAngle, sinAngle ) + self.x
        y2 = self.__transformY( xPlus, yPlus, cosAngle, sinAngle ) + self.y
        
        # Point 3.
        x3 = self.__transformX( xMinus, yPlus, cosAngle, sinAngle ) + self.x
        y3 = self.__transformY( xMinus, yPlus, cosAngle, sinAngle ) + self.y
        
        # Draw.
        canvas.create_polygon( x0, y0, x1, y1, x2, y2, x3, y3, fill = 'white', outline = 'black' )
        
    def __transformX( self, x, y, cosAngle, sinAngle ):
        return x * cosAngle - y * sinAngle
        
    def __transformY( self, x, y, cosAngle, sinAngle ):
        return y * cosAngle + x * sinAngle 
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()