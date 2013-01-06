from .movestate import *

class MoveHeun:
    """ Integration for moveable objects with position x and velocity v. """
    
    @staticmethod
    def integrate( state, derivative, h ):
        """ Integrate using the heun method.

        Arguments:
        state -- The current state (MoveState).
        derivative -- The current derivative (MoveState).
        h -- The change in step number (float).
        
        Returns the new state and the new derivative.
        """
    
        bad = state + derivative * h
        badDerivative = MoveState()
        badDerivative.position = bad.velocity # Derivative of position is velocity.
        badDerivative.velocity = derivative.velocity
        
        new = state + (derivative + badDerivative) * (h / 2)
        newDerivative = MoveState()
        newDerivative.position = new.velocity # Derivative of position is velocity.
        newDerivative.velocity = derivative.velocity
        return new, newDerivative