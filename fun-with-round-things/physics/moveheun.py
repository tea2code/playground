class MoveHeun:
    """ Integration for moveable objects with position x and velocity v. """
    
    @staticmethod
    def integrate(  state, derivative, h, derivativeClass ):
        """ Integrate using the heun method.

        Arguments:
        state -- The current state.
        derivative -- The current derivative.
        h -- The change in step number.
        derivativeClass -- Class for derivatives.
        
        Returns the new state and the new derivative.
        """
    
        bad = state + derivative * h
        badDerivative = derivativeClass()
        badDerivative.x = bad.v # Derivative of position is velocity.
        badDerivative.v = derivative.v
        
        new = state + (derivative + badDerivative) * (h / 2)
        newDerivative = derivativeClass()
        newDerivative.x = new.v # Derivative of position is velocity.
        newDerivative.v = derivative.v
        return new, newDerivative