import tickable
from tkinter import *

class TkGraphics( tickable.Tickable ):
    """ This class handles the visualisation of the current state. 
    
    Member:
    canvas -- The canvas object.
    window -- The window object.
    """
    
    def __init__( self, data ):
        """ The parameter data which contains the window settings. """
        self.window = Tk()
        self.window.title( data.windowTitle )
        self.canvas = Canvas( self.window, width = data.windowWidth, height = data.windowHeight )
        self.canvas.pack()
    
    def tick( self, data ):
        """ Implementation of Tickable.tick().

        Draws the current state (data) on the canvas. """
        self.canvas.delete( ALL )
        self.canvas.configure( background = 'white' )
        
        for circle in data.circles:
            x = circle.position.x
            y = circle.position.y
            r = circle.radius
            c = circle.color
            self.canvas.create_oval( x - r, y - r, x + r, y + r, width = r, fill = c, outline = c )
            
        self.window.title( data.windowTitle + ' (FPS ' + str(data.fps) + ')' )