import random
import tickable

class Physics( tickable.Tickable ):
    """ This class calculates the physical reactions of all objects. """

    def tick( self, data ):
        """ Implementation of Tickable.tick().

        Calculates the physic on all objects. """
        for circle in data.circles:
            circle.position.x += self.__randomInteger()

    def __randomInteger( self ):
        """ Private helper method which returns a random integer between -5 and 5. """
        # Create random integer and shift by 5.
        return round( random.random() * 10 ) - 5 