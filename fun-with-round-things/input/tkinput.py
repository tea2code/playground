from common import vector2d

class TkInput():
    ''' This class handles input events from tkinter. 
    
    Member:
    data -- The data object.
    '''
    
    data = None
    
    def __init__( self, data, window ):
        ''' Initializes input module with the data object and binds input event callbacks 
        to window. '''
        self.data = data
        window.bind( '<B1-Motion>', self.__mouseMotion )
        window.bind( '<ButtonPress-1>', self.__mousePressed )
        window.bind( '<ButtonRelease-1>', self.__mouseReleased )
    
    def __mouseMotion( self, event ):
        ''' Handles mouse motion while button is pressed. '''
        self.data.mousePosition.x = event.x
        self.data.mousePosition.y = event.y
    
    def __mousePressed( self, event ):
        ''' Handles mouse button pressed event. '''
        self.data.mousePressed = True
        self.data.mousePosition.x = event.x
        self.data.mousePosition.y = event.y
    
    def __mouseReleased( self, event ):
        ''' Handles mouse button pressed event. '''
        self.data.mousePressed = False
        force = self.data.mousePosition - self.data.circle.position
        force = force * 42
        self.data.circle.addForce( force )