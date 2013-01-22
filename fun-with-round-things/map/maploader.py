import xml.sax as sax

from map import mapparser

class MapLoader():
    ''' Loads maps from files. '''
    
    def load( self, mapFile ):
        ''' Loads the given map file. Throws SAXParseException in case of an error. 
        Returns the game object. '''
        handler = mapparser.MapParser() 
        parser = sax.make_parser() 
        parser.setContentHandler( handler ) 
        parser.parse( mapFile ) 
        return handler.game