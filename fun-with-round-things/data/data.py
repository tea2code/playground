from common.vector2d import *

class Data:
    ''' This class represents all the data available in the current game which is equivalent to 
    the current state. 
    
    Member:
    circles -- A list of circle objects.
    deltaTime -- The time difference since the last step.
    fps -- The current frame rate.
    game -- The game object.
    target -- The target to hit.
    time -- The accumulated time of all steps.
    windowHeight -- Height of the window.
    windowTitle -- Title of the window.
    windowWidth -- Width of the window.
    '''

    circles = []
    deltaTime = 0
    fps = 0
    game = None
    target = Vector2d.nullVector()
    time = 0
    timeLimit = 0
    windowHeight = 0
    windowTitle = ''
    windowWidth = 0
    
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
        >>> d.target.x == 0 and d.target.y == 0
        True
        >>> d.time
        0
        >>> d.timeLimit
        0
        >>> d.windowHeight
        0
        >>> d.windowTitle
        ''
        >>> d.windowWidth
        0
        '''
    
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()