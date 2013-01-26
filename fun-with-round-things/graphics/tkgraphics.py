from common import tickable
from data import rect as datarect
from graphics import border
from graphics import rect 

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
        self.canvas = tkinter.Canvas( self.window, width = data.game.world.width, height = data.game.world.height )
        self.canvas.pack(),
        self.canvas.configure( background = 'white' )
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Draws the current state (data) on the canvas. Throws TypeError if game.world.map.objects
        contains an unknown type. '''
        
        # Reset everything.
        self.canvas.delete( tkinter.ALL )
        
        # Draw circles.
        for circle in data.circles:
            x = circle.position.x
            y = circle.position.y
            r = circle.radius
            c = circle.color
            self.canvas.create_oval( x - r, y - r, x + r, y + r, width = r, fill = c, outline = c )
            
        # Draw target.
        target = data.game.world.target
        self.canvas.create_line( target.x - 5, target.y,     target.x + 5, target.y     )
        self.canvas.create_line( target.x,     target.y - 5, target.x,     target.y + 5 )
            
        # Draw borders.
        b = border.Border( data.game.world.map.border )
        b.draw( self.canvas )
        
        # Draw objects.
        for object in data.game.world.map.objects:
            if isinstance( object, datarect.Rect ):
                r = rect.Rect( object.angle, object.height, object.width, 
                               object.position.x, object.position.y )
                r.draw( self.canvas )
            else:
                raise TypeError( 'Unknown object "{0}" in map'.format(object) )
            
        # Set window title with current frames per second.
        self.window.title( data.windowTitle + ' (FPS ' + str(data.fps) + ')' )