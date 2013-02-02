from common import vector2d

class Data:
    ''' This class represents all the data available in the current game which is equivalent to 
    the current state. 
    
    Member:
    circle -- The player entity aka the circle.
    collisions -- A list of collision objects.
    deltaTime -- The time difference since the last step.
    fps -- The current frame rate.
    game -- The game object.
    mousePosition -- The current mouse position if pressed.
    mousePressed -- True if mouse button is pressed.
    time -- The accumulated time of all steps.
    windowTitle -- Title of the window.
    '''

    circle = None
    collisions = []
    deltaTime = 0
    fps = 0
    game = None
    mousePosition = vector2d.Vector2d.nullVector()
    mousePressed = False
    time = 0
    windowTitle = ''
    
    def __init__( self ):
        ''' Test: 
        >>> d = Data()
        >>> d.circle
        >>> len(d.collisions)
        0
        >>> d.deltaTime
        0
        >>> d.fps
        0
        >>> d.game
        >>> d.mousePosition.x == 0 and d.mousePosition.y == 0
        True
        >>> d.mousePressed
        False
        >>> d.time
        0
        >>> d.windowTitle
        ''
        '''
    
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()