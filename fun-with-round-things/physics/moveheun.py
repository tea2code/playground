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
        badDerivative.x = bad.v # Derivative of position is velocity.
        badDerivative.v = derivative.v
        
        new = state + (derivative + badDerivative) * (h / 2)
        newDerivative = MoveState()
        newDerivative.x = new.v # Derivative of position is velocity.
        newDerivative.v = derivative.v
        return new, newDerivative