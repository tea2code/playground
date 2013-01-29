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
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()