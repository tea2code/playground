import time
from collections import deque

class FpsCounter():
    """ This class implements a counter which calculates the frames per second. """
    
    measurements = deque([])
    
    def __init__( self, maxNum = 20 ):
        """ Parameter maxNum gives the maximum number of stored measurements. """
        self.maxNum = maxNum
        
    def fps( self ):
        """ Calculates the frames per second returns it as a floating point number. """
        sumM = sum( self.measurements )
        lenM = len( self.measurements )
        avgM =  sumM / lenM
        return 1 / avgM
        
    def start( self ):
        """ Starts counter. """
        self.lastTime = self.__time()
        
    def tick( self ):
        """ Must be called every frame. """
        currentTime = self.__time()
        self.measurements.append( currentTime - self.lastTime )
        self.lastTime = currentTime
        
        if len(self.measurements) > self.maxNum:
            self.measurements.popleft()
        
    def __time( self ):
        return time.perf_counter()