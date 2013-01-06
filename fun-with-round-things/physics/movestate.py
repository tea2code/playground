class MoveState:
    """ State class for integration of movable objects. """
    
    x = 0
    v = 0

    def __add__( self, other ):
        new = MoveState()
        new.x = self.x + other.x
        new.v = self.v + other.v
        return new
    
    def __mul__( self, scalar ):
        new = MoveState()
        new.x = self.x * scalar
        new.v = self.v * scalar
        return new