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
                state.position = circle.position.x
                state.velocity = circle.velocity.x
                
                derivative = MoveState()
                derivative.position = state.velocity # Derivative of position is velocity.
                derivative.velocity = data.acceleration # Derivative of velocity is acceleration.
                
                newState, newDerivative = MoveHeun.integrate( state, derivative, data.deltaTime )
                circle.position.x = newState.position
                circle.velocity.x = newState.velocity