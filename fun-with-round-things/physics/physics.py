import random
from . import moveheun
from . import movestate
from common import tickable

class Physics( tickable.Tickable ):
    ''' This class calculates the physical reactions of all objects. '''

    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Calculates the physic on all objects. '''

        for circle in data.circles:
            state = movestate.MoveState()
            state.force = circle.sumForces()
            state.mass = circle.mass
            state.momentum = circle.momentum
            state.position = circle.position

            newState = moveheun.MoveHeun.integrate( state, data.deltaTime )
            circle.momentum = newState.momentum
            circle.position = newState.position