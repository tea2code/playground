""" This abstract class defines a methods to get access to the global data object. Must be implemented
    by every data accessor. You should only use the getter/setter methods. """
class AbstractDataAccessor:
    data = None
    
    """ Returns the data object. """
    def getData( self ):
        return self.data
        
    """ Sets the data object and returns the object. """
    def setData( self, data ):
        self.data = data
        return self