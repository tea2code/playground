﻿from common import tickable
from common import vector2d

class GameRules( tickable.Tickable ):
    ''' Controls the rules in a game. '''
    
    def tick( self, data ):
        ''' Implementation of Tickable.tick().

        Checks the game rules.'''
        