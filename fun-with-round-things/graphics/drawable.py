from abc import ABCMeta, abstractmethod  

class Drawable(metaclass = ABCMeta):
    ''' Base class for drawable objects. '''
    
    @abstractmethod
    def draw( self, canvas ):
        ''' The derived class must implement this method. Receives the canvas to draw on. '''