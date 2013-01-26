from graphics import drawable

class Border( drawable.Drawable ):
    ''' Draws the border of a map. 
    
    Member:
    width -- The width of the border.
    '''
    
    width = 0
    
    def __init__( self, width ):
        ''' Constructor which sets the width of the border.

        Test:
        >>> b = Border( 10 )
        >>> b.width
        10
        '''
        self.width = width
        
    def draw( self, canvas ):
        ''' Draws the border on the given canvas. '''
        
        if self.width <= 0:
            return
        
        x0 = self.width
        y0 = self.width
        x1 = int( canvas.cget('width') ) - self.width
        y1 = int( canvas.cget('height') ) - self.width
        canvas.create_rectangle( x0, y0, x1, y1 )
     
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()