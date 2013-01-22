class Map:
    ''' This represents the actual map.

    Member:
    border -- Width of the map border (int).
    objects -- List of objects in this map. Can be movable or static.
    '''
    border = 1
    objects = []
    
    def __init__( self ):
        ''' Test:
        >>> m = Map()
        >>> m.border
        1
        >>> len(m.objects)
        0
        '''
    
    def __str__( self ):
        ''' Test:
        >>> m = Map()
        >>> print(m)
        Map(border 1.00, objects [])
        '''
        objectsString = ", ".join( [str(element) for element in self.objects]  )
        return 'Map(border {0:.2f}, objects [{1}])'.format(self.border, objectsString)
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()