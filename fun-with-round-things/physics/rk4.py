class Rk4:

    @staticmethod
    def nextStep( x, h, y, f ):
        """ Integrates the next step of a function using the common fourth-order Runge–Kutta method.

        Arguments:
        x -- The current step number.
        h -- The change in step number.
        y -- The current state.
        f -- The function to integrate.
        
        Returns a pair of values. First value is the new step number. Second value is the new state.
        """
        k1 = h * f( x, y )
        k2 = h * f( x + 0.5 * h, y + 0.5 * k1 )
        k3 = h * f( x + 0.5 * h, y + 0.5 * k2 )
        k4 = h * f( x + h, y + k3 )
        return x + h, y + (k1 + 2*(k2 + k3) + k4) / 6.0