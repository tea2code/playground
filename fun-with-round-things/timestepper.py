import time

class Timestepper:
    """ Calls a function based on predefined time steps. This function does not contain a automatic timer.
    Instead it checks the elapsed time and executes the function only if enough time was elapsed. The function
    will be executed as long time is left in this frame.
    
    Member:
    accumulator -- Accumulates the frame times.
    maxFrameTime -- Maximum frame time to avoid spiral of death.
    t -- The current time.
    """

    accumulator = 0.0
    maxFrameTime = 0.25
    t = 0.0
    
    def __init__( self, dt, func ):
        """ Parameter:
        dt -- The target difference between two frames.
        func -- The function to execute. It must take two parameters: t, dt
        """
        self.dt = dt
        self.func = func
        
    def start( self ):
        """ Start the stepper. """
        self.currentTime = self.__hiresTime()
        
    def tick( self ):
        """ Calls function based on elapsed time. """
        newTime = self.__hiresTime()
        frameTime = min( newTime - self.currentTime, self.maxFrameTime )
        self.currentTime = newTime
        
        self.accumulator += frameTime
        
        while self.accumulator >= self.dt:
            self.func( self.t, self.dt )
            self.t += self.dt
            self.accumulator -= self.dt
    
    def __hiresTime( self ):
        return time.perf_counter()