import common.timestepper
import common.vector2d
import data.circle
import data.data
import data.game
import data.map
import data.movable
import data.rect
import data.world
import fps.fps
import fps.fpscounter
import gamerules.gamestarter
import map.mapparser
import physics.movestate

if __name__ == '__main__':
    import doctest
    doctest.testmod( common.timestepper )
    doctest.testmod( common.vector2d )
    doctest.testmod( data.circle )
    doctest.testmod( data.data )
    doctest.testmod( data.game )
    doctest.testmod( data.map )
    doctest.testmod( data.movable )
    doctest.testmod( data.rect )
    doctest.testmod( data.world )
    doctest.testmod( fps.fps )
    doctest.testmod( fps.fpscounter )
    doctest.testmod( gamerules.gamestarter )
    doctest.testmod( physics.movestate )
    doctest.testmod( map.mapparser )