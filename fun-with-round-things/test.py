import common.timestepper
import common.vector2d
import data.circle
import data.movable
import fps.fps
import fps.fpscounter
import physics.movestate

if __name__ == '__main__':
    import doctest
    doctest.testmod( common.timestepper )
    doctest.testmod( common.vector2d )
    doctest.testmod( data.circle )
    doctest.testmod( data.movable )
    doctest.testmod( fps.fps )
    doctest.testmod( fps.fpscounter )
    doctest.testmod( physics.movestate )