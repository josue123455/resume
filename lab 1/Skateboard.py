#Josue Andaluz
#190250
#Lab 1 data structures
#worked with megan and kameeri

from abc import ABC, abstractmethod
from Vehicle import Vehicle

class Skateboard(Vehicle):
    def __init__(self, top_speed, location, direction):
       super().__init__(3,top_speed, location, direction)

    def accelerate(self):
        if self._current_speed <= self._top_speed:
            self._current_speed += (int(self._top_speed) * 0.5)
        else:
            self._current_speed += (int(self._top_speed) * 0.5)
        
    def decelerate(self):
        self._current_speed = 0.0
