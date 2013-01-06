import time

class Timestepper:
    """ Calls a function based on predefined time steps. This function does not contain a automatic timer.
    Instead it checks the elapsed time and executes the function only if enough time was elapsed. The function
    will be executed as long time is left in this frame.
    
    Member:
    accumulator -- Accumulates the frame times.
    deltaTime -- The target difference between two frames.
    func -- The function to execute. Must take time and deltaTime as parameter.
    maxFrameTime -- Maximum frame time to avoid spiral of death.
    time -- The accumulated time.
    _currentTime -- The current timestamp.
    """

    accumulator = 0
    deltaTime = 0
    func = None
    maxFrameTime = 0.25
    time = 0
    _currentTime = 0
    
    def __init__( self, deltaTime, func ):
        """ Test:
        >>> t = Timestepper( 0.1, lambda t, dt: t + dt )
        >>> t.deltaTime
        0.1
        >>> t.func # doctest: +ELLIPSIS
        <function <lambda> at 0x...>
        """
        self.deltaTime = deltaTime
        self.func = func
        
    def start( self ):
        """ Start the stepper. 
        
        Test:
        >>> t = Timestepper( 0.1, lambda t, dt: t + dt )
        >>> t._currentTime > 0
        False
        >>> t.start()
        >>> t._currentTime > 0
        True
        """
        self._currentTime = self.__hiresTime()
        
    def tick( self ):
        """ Calls function based on elapsed time. """
        newTime = self.__hiresTime()
        frameTime = min( newTime - self._currentTime, self.maxFrameTime )
        self._currentTime = newTime
        
        self.accumulator += frameTime
        
        while self.accumulator >= self.deltaTime:
            self.func( self.time, self.deltaTime )
            self.time += self.deltaTime
            self.accumulator -= self.deltaTime
    
    def __hiresTime( self ):
        return time.perf_counter()
        
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()