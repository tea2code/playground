from common.vector2d import *

class Rect:
    ''' A non-movable rect object. 
    
    Member:
    angle -- The angle in degree of the rect (int).
    height -- The height of the rect (int).
    position -- The position/center of the rect (Vector2d).
    width -- The width of the rect (int).
    '''
    angle = 0
    height = 1
    position = None
    width = 1
    
    def __init__( self ):
        position = Vector2d.nullVector()