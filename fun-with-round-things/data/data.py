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