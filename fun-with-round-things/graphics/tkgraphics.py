from common import tickable

import tkinter

class TkGraphics( tickable.Tickable ):
    ''' This class handles the visualisation of the current state. 
    
    Member:
    canvas -- The canvas object.
    window -- The window object.
    '''
    
    window = None
    canvas = None
    
    def __init__( self, data ):
        ''' The parameter data which contains the window settings. '''
        self.window = tkinter.Tk()
        self.window.title( data.windowTitle )
        self.canvas = tkinter.Canvas( self.window, width = data.windowWidth, height = data.windowHeight )
        self.canvas.pack(),
        self.canvas.configure( background = 'white' )
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Draws the current state (data) on the canvas. '''
        self.canvas.delete( tkinter.ALL )
        
        for circle in data.circles:
            x = circle.position.x
            y = circle.position.y
            r = circle.radius
            c = circle.color
            self.canvas.create_oval( x - r, y - r, x + r, y + r, width = r, fill = c, outline = c )
            
        self.canvas.create_line( data.target.x - 5, data.target.y, data.target.x + 5, data.target.y )
        self.canvas.create_line( data.target.x, data.target.y - 5, data.target.x, data.target.y + 5 )
            
        self.window.title( data.windowTitle + ' (FPS ' + str(data.fps) + ')' )