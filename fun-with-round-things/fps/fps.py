from common import tickable
from . import fpscounter

class Fps( tickable.Tickable ):
    """ This class calculates the frame rate. """

    started = False
    
    def __init__( self, maxTickCounts, measurementPoints ):
        self.tickCounter = 0
        self.maxTickCounts = maxTickCounts
        self.fpsCounter = fpscounter.FpsCounter( measurementPoints )
    
    def tick( self, data ):
        """ Implementation of Tickable.tick(). """
        
        if self.started == False:
            self.fpsCounter.start()
            self.started = True
        
        self.fpsCounter.tick()
        self.tickCounter += 1
        if self.tickCounter > self.maxTickCounts:
            data.fps = round( self.fpsCounter.fps() )
            self.tickCounter = 0