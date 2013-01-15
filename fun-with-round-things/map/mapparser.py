import xml.sax as sax

class MapParser( sax.handler.ContentHandler ):
    ''' This parser creates a representation of a xml file.

    Member:
    
    '''
    content = ''
    result = []
    tag = ''

    def startElement( self, name, attrs ): 
        

    def endElement (self, name ): 
        

    def characters( self, content ): 
        