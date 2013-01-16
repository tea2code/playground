from common.vector2d import *

class Map:
    ''' This represents the actual map.

    Member:
    border -- Width of the map border (int).
    objects -- List of objects in this map. Can be movable or static.
    '''
    border = 1
    objects = []