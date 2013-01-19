class Rk4:

    @staticmethod
    def integrate( x, h, state, func ):
        ''' Integrates the next step of a function using the common fourth-order Runge–Kutta method.

        Arguments:
        x -- The current step number.
        h -- The change in step number.
        state -- The current state.
        func -- The function to integrate. This function must take x, h, state and (optional) derivate as parameters. Must return the derivate.
        
        Returns the new state.
        '''
        k1 = func( x, 0, state )
        k2 = func( x, 0.5 * h, state, k1 )
        k3 = func( x, 0.5 * h, state, k2 )
        k4 = func( x, h, state, k3 )
        return state + ((k1 + (k2 + k3) * 2 + k4) * (1 / 6) * h)