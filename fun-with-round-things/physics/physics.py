import random
from .rk4 import *
from .circlerk4state import *
from common import tickable

class Physics( tickable.Tickable ):
    """ This class calculates the physical reactions of all objects. """

    counter = 0
    
    def tick( self, data ):
        """ Implementation of Tickable.tick().

        Calculates the physic on all objects. """
        
        self.acceleration = data.acceleration
        pos = ''
        
        if data.time < data.timeLimit + 0.00001:
            for circle in data.circles:
                state = CircleRk4State()
                state.x = circle.position.x
                state.v = circle.velocity.x
                
                newState = Rk4.integrate( data.time, data.deltaTime, state, self.__evaluate, CircleRk4State )
                circle.position.x = newState.x
                circle.velocity.x = newState.v
                
                pos += '(%.5f, %.5f) at %.5fm/s; ' % (circle.position.x, circle.position.y, circle.velocity.x)
          
        print( '[%03d] Time: %0.5fs, Circles: %s' % (self.counter, data.time, pos) )
          
        self.counter += 1
        
    def __evaluate( self, t, dt, state, derivative ):
        new = CircleRk4State()
        new.x = state.x + derivative.x * dt
        new.v = state.v + derivative.v * dt
        newDerivative = CircleRk4State()
        newDerivative.x = new.v
        newDerivative.v = self.acceleration
        return newDerivative