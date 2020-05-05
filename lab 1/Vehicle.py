#Josue Andaluz
#190250
#Lab 1 data structures
#worked with megan and kameeri

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, length,top_speed, location, direction):
        self._length = length
        self._top_speed = top_speed
        self._location = location
        self._direction = direction
        self._current_speed = 0
        
    def get_length(self):
        return self._length
        
    def get_top_speed(self):
        return self._top_speed
        
    def get_location(self):
        return self._location
        
    def get_direction (self):
        return self._direction
        
    def get_current_speed(self):
        return self._current_speed

    def turn_left(self):
        if self._direction == "NORTH":
            self._direction = "WEST"
        elif self._direction =="SOUTH":
            self._direction = "EAST"
        elif self._direction == "WEST":
            self._direction = "SOUTH"
        elif self._direction == "EAST":
            self._direction = "NORTH"

    def turn_right(self):
        if self._direction == "NORTH":
            self._direction = "EAST"
        elif self._direction == "SOUTH":
            self._direction = "WEST"
        elif self._direction == "WEST":
            self._direction = "NORTH"
        elif self._direction == "EAST":
            self._direction = "SOUTH"
                
    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def decelerate(self):
        pass

    def move(self):
        if self._direction == "SOUTH":
            self._location= (self._location[0], self._location[1] - self._current_speed)
        if self._direction == "NORTH":
            self._location= (self._location[0], self._location[1] + self._current_speed)
        if self._direction == "WEST":
            self._location= (self._location[0] - self._current_speed, self._location[1])
        if self._direction == "EAST":
            self._location= (self._location[0] + self._current_speed, self._location[1])

