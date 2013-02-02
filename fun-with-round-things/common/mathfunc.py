import math

class MathFunc:
    ''' Collection of stand alone math functions. '''
    
    @staticmethod
    def euclideanDistance( x1, y1, x2, y2 ):
        ''' Calculates the euclidean distance between two points in second dimension.

        Test:
        >>> '{0:.4f}'.format( MathFunc.euclideanDistance(2, -1, -2, 2) )
        '5.0000'
        '''
        a = math.fabs( x1 - x2 )
        b = math.fabs( y1 - y2 )
        c = math.sqrt( (a * a) + (b * b) )
        return c
        
    @staticmethod
    def rotateX( x, y, angle ):
        ''' Rotates the x-component of a coordinate using the angle (degree). Positiv direction is 
        counterclock wise.

        Test:
        >>> print( '{0:.2f}'.format(MathFunc.rotateX(0, 1, 90)) )
        -1.00
        >>> print( '{0:.2f}'.format(MathFunc.rotateX(0, 1, 180)) )
        -0.00
        '''
        angleRadian = math.radians( angle )
        return x * math.cos( angleRadian ) - y * math.sin( angleRadian )
        
    @staticmethod
    def rotateY( x, y, angle ):
        ''' Rotates the y-component of a coordinate using the angle (degree). Positiv direction is 
        counterclock wise.

        Test:
        >>> print( '{0:.2f}'.format(MathFunc.rotateY(0, 1, 90)) )
        0.00
        >>> print( '{0:.2f}'.format(MathFunc.rotateY(0, 1, 180)) )
        -1.00
        '''
        angleRadian = math.radians( angle )
        return y * math.cos( angleRadian ) + x * math.sin( angleRadian )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()