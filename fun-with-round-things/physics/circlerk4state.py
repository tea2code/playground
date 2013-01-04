class CircleRk4State:
    """ State class for RK4. """
    
    x = 0
    v = 0

    def __add__( self, other ):
        new = CircleRk4State()
        new.x = self.x + other.x
        new.v = self.v + other.v
        return new
    
    def __mul__( self, scalar ):
        new = CircleRk4State()
        new.x = self.x * scalar
        new.v = self.v * scalar
        return new