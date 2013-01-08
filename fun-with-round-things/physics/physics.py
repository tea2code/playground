import random
from .moveheun import *
from .movestate import *
from common import tickable

class Physics( tickable.Tickable ):
    """ This class calculates the physical reactions of all objects. """

    def tick( self, data ):
        """ Implementation of Tickable.tick().

        Calculates the physic on all objects. """

        if data.time < data.timeLimit + 0.00001:
            for circle in data.circles:
                state = MoveState()
                state.force = circle.sumForces()
                state.mass = circle.mass
                state.momentum = circle.momentum
                state.position = circle.position
 
                newState = MoveHeun.integrate( state, data.deltaTime )
                circle.momentum = newState.momentum
                circle.position = newState.position
                
                # circle.clearForces()