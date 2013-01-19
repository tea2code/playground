class Game:
    ''' This represents a single game like a level/map. 
    
    Member:
    author -- Author of this game (string).
    date -- Date of creation (string).
    description -- Description of this game (string).
    name -- Name of this game (string).
    version -- Current version of this game (string).
    world -- The world object (World).
    '''
    author = ''
    date = ''
    description = ''
    name = ''
    version = ''
    world = None
    
    def __init__( self ):
        ''' Test:
        >>> g = Game()
        >>> g.author
        ''
        >>> g.date
        ''
        >>> g.description
        ''
        >>> g.name
        ''
        >>> g.version
        ''
        >>> g.world
        '''
        
    def __str__( self ):
        ''' Test:
        >>> g = Game()
        >>> print(g)
        Game(author , date , description , name , version , world None)
        '''
        return 'Game(author {0}, date {1}, description {2}, name {3}, version {4}, world {5})'.format( self.author, self.date, self.description, self.name, self.version, self.world )
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()