from common import vector2d

class Data:
    ''' This class represents all the data available in the current game which is equivalent to 
    the current state. 
    
    Member:
    circles -- A list of circle objects.
    deltaTime -- The time difference since the last step.
    fps -- The current frame rate.
    game -- The game object.
    time -- The accumulated time of all steps.
    windowTitle -- Title of the window.
    '''

    circles = []
    deltaTime = 0
    fps = 0
    game = None
    time = 0
    windowTitle = ''
    
    def __init__( self ):
        ''' Test: 
        >>> d = Data()
        >>> len(d.circles)
        0
        >>> d.deltaTime
        0
        >>> d.fps
        0
        >>> d.game
        >>> d.time
        0
        >>> d.windowTitle
        ''
        '''
    
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()