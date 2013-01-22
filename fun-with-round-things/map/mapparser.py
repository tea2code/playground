import xml.sax as sax

from common import vector2d
from data import game
from data import map
from data import rect
from data import world

class MapParser( sax.handler.ContentHandler ):
    ''' This parser creates a representation of a xml map. If an parsing error occures any method 
    can throw a SAXParseException.

    Constants:
    ATTR_PARSER
    PARSER_VERSION -- The parser version.
    TAG_ANGLE
    TAG_AUTHOR
    TAG_BORDER
    TAG_DATE
    TAG_DESCRIPTION
    TAG_GAME
    TAG_HEIGHT
    TAG_MAP
    TAG_NAME
    TAG_RECT
    TAG_START
    TAG_TARGET
    TAG_TIMELIMIT
    TAG_VERSION
    TAG_WIDTH
    TAG_WORLD
    TAG_X
    TAG_Y
    
    Member:
    game -- The resulting game object.
    _content -- The content of the current tag (String).
    _elementStack -- A stack containing the current element and all of its parents.
    _errorUnknown -- Error text for unknown tag.
    _errorVersion -- Error text for not parsable engine version.
    '''
    ATTR_PARSER = 'parser'
    PARSER_VERSION = 1
    TAG_ANGLE = 'angle'
    TAG_AUTHOR = 'author'
    TAG_BORDER = 'border'
    TAG_DATE = 'date'
    TAG_DESCRIPTION = 'description'
    TAG_GAME = 'game'
    TAG_HEIGHT = 'height'
    TAG_MAP = 'map'
    TAG_NAME = 'name'
    TAG_RECT = 'rect'
    TAG_START = 'start'
    TAG_TARGET = 'target'
    TAG_TIMELIMIT = 'timelimit'
    TAG_VERSION = 'version'
    TAG_WIDTH = 'width'
    TAG_WORLD = 'world'
    TAG_X = 'x'
    TAG_Y = 'y'
    
    game = None    
    _content = ''
    _elementStack = []
    _errorUnknown = 'Unknown element "{0}"'
    _errorVersion = 'Not parsable version "{0}"'
    _vectorContent = None
    
    def __init__( self ):
        ''' Test:
        >>> m = MapParser()
        >>> m.game
        >>> m._content
        ''
        >>> len(m._elementStack)
        0
        >>> m._vectorContent
        '''
        super().__init__()
    
    def startElement( self, name, attrs ): 
        self._content = ''
        if len(self._elementStack) == 0 or self._elementStack[-1] == self.TAG_GAME:
            self.__gameStart( name, attrs )
        elif self._elementStack[-1] == self.TAG_WORLD: 
            self.__worldStart( name, attrs )
        elif self._elementStack[-1] == self.TAG_MAP: 
            self.__mapStart( name, attrs )
        elif self._elementStack[-1] == self.TAG_RECT:
            self.__rectStart( name, attrs )
        else:
            raise sax.SAXParseException( self._errorUnknown % (name) )

    def endElement (self, name ): 
        if self._elementStack[-1] == self.TAG_GAME:
            self.__gameEnd( name )
        elif self._elementStack[-1] == self.TAG_WORLD: 
            self.__worldEnd( name )
        elif self._elementStack[-1] == self.TAG_MAP: 
            self.__mapEnd( name )
        elif self._elementStack[-1] == self.TAG_RECT: 
            self.__rectEnd( name )    
        else:
            raise sax.SAXParseException( self._errorUnknown % (name) )

    def characters( self, content ): 
        self._content += content
        
    def __gameEnd( self, name ):
        if name == self.TAG_AUTHOR:
            self.game.author = self._content
        elif name == self.TAG_DATE:
            self.game.date = self._content
        elif name == self.TAG_DESCRIPTION:
            self.game.description = self._content
        elif name == self.TAG_NAME:
            self.game.name = self._content
        elif name == self.TAG_VERSION:
            self.game.version = self._content
        else:
            if name == self.TAG_GAME:
                self._elementStack.pop()
            else:
                raise sax.SAXParseException( self._errorUnknown % (name) )
    
    def __gameStart( self, name, attrs ):
        if name == self.TAG_GAME:
            if int(attrs[self.ATTR_PARSER]) <= self.PARSER_VERSION:
                self._elementStack.append( name )
                self.game = game.Game()
            else:
                raise sax.SAXParseException( self._errorVersion % (attrs.get(self.ATTR_PARSER)) )
        elif name == self.TAG_WORLD:
            self._elementStack.append( name )
            self.game.world = world.World()
        else:
            if name not in [self.TAG_AUTHOR, self.TAG_DATE, self.TAG_DESCRIPTION, self.TAG_NAME, 
                            self.TAG_VERSION]:
                raise sax.SAXParseException( self._errorUnknown % (name) )
        
    def __mapEnd( self, name ):
        if name == self.TAG_BORDER:
            self.game.world.map.border = float(self._content)
        else:
            if name == self.TAG_MAP:
                self._elementStack.pop()
            else:
                raise sax.SAXParseException( self._errorUnknown % (name) )
    
    def __mapStart( self, name, attrs ):
        if name == self.TAG_RECT:
            self._elementStack.append( name )
            self.game.world.map.objects.append( rect.Rect() )
        else:
            if name not in [self.TAG_BORDER]:
                raise sax.SAXParseException( self._errorUnknown % (name) )
    
    def __rectEnd( self, name ):
        if name == self.TAG_ANGLE:
            self.game.world.map.objects[-1].angle = float(self._content)
        elif name == self.TAG_HEIGHT:
            self.game.world.map.objects[-1].height = float(self._content)
        elif name == self.TAG_WIDTH:
            self.game.world.map.objects[-1].width = float(self._content)
        elif name == self.TAG_X:
            self.__vectorX( self._content )
        elif name == self.TAG_Y:
            self.__vectorY( self._content )
        else:
            if name == self.TAG_RECT:
                self.game.world.map.objects[-1].position = self._vectorContent
                self._elementStack.pop()
            else:
                raise sax.SAXParseException( self._errorUnknown % (name) )
    
    def __rectStart( self, name, attrs ):
        if name not in [self.TAG_ANGLE, self.TAG_HEIGHT, self.TAG_WIDTH, self.TAG_X, self.TAG_Y]:
            raise sax.SAXParseException( self._errorUnknown % (name) )
    
    def __vectorX( self, x ):
        if self._vectorContent is None:
            self._vectorContent = vector2d.Vector2d.nullVector()
        self._vectorContent.x = float(x)
    
    def __vectorY( self, y ):
        if self._vectorContent is None:
            self._vectorContent = vector2d.Vector2d.nullVector()
        self._vectorContent.y = float(y)
    
    def __worldEnd( self, name ):
        if name == self.TAG_HEIGHT:
            self.game.world.height = float(self._content)
        elif name == self.TAG_START:
            self.game.world.start = self._vectorContent
            self._vectorContent = None
        elif name == self.TAG_TARGET:
            self.game.world.target = self._vectorContent
            self._vectorContent = None
        elif name == self.TAG_TIMELIMIT:
            self.game.world.timelimit = float(self._content)
        elif name == self.TAG_WIDTH:
            self.game.world.width = float(self._content)
        elif name == self.TAG_X:
            self.__vectorX( self._content )
        elif name == self.TAG_Y:
            self.__vectorY( self._content )
        else:
            if name == self.TAG_WORLD:
                self._elementStack.pop()
            else:
                raise sax.SAXParseException( self._errorUnknown % (name) )
    
    def __worldStart( self, name, attrs ):
        if name == self.TAG_MAP:
            self._elementStack.append( name )
            self.game.world.map = map.Map()
        else:
            if name not in [self.TAG_HEIGHT, self.TAG_WIDTH, self.TAG_START, self.TAG_TARGET, 
                            self.TAG_TIMELIMIT, self.TAG_X, self.TAG_Y]:
                raise sax.SAXParseException( self._errorUnknown % (name) )
                
if __name__ == '__main__':
    print( 'Executing doctest.' )
    import doctest
    doctest.testmod()