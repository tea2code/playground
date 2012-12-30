import tickable
from tkinter import *

class Graphics( tickable.Tickable ):
    """ This class handles the visualisation of the current state. """
    
    def __init__( self, canvas ):
        """ The parameter canvas is the tkinter canvas to draw on. """
        self.canvas = canvas
    
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