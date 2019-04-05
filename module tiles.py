# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:15:09 2019

@author: sleaf
"""

import items, enemies
 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def intro_text(self):
        raise NotImplementedError()
        
    def modify_player(self, player):
        raise NotImplementedError()