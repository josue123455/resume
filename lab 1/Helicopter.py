#Josue Andaluz
#190250
#Lab 1 data structures
#worked with megan and kameeri

from abc import ABC, abstractmethod
from Vehicle import Vehicle

class Helicopter(Vehicle):
    def __init__(self, length, top_speed, location, direction, acceleration_factor):
        super().__init__(length, top_speed, location, direction)

        self._acceleration_factor = acceleration_factor
        self._registration_number = ""
        self._owner = ""
        self._altitude = 0.0

    def get_acceleration(self):
        return self._acceleration_factor
        
    def get_registration_number(self):
        return self._registration_number

    def get_owner(self):
         return self._owner

    def get_altitude(self):
        return self._altitude
        
    def change_altitude(self, new_alt):
        if self._altitude + (new_alt) <= 0.0:
            self._altitude = 0.0
        else:
            self._altitude += float(new_alt)

    def set_registration_number(self, reg_num):
        self._registration_number = str(reg_num)

    def set_owner(self, owner):
        self._owner = str(owner)
                
    def turn_right(self):
        super().move()
        super().turn_right()
    
    def turn_left(self):
        super().move()
        super().turn_left()

    def accelerate(self):
        if self._current_speed >= self._top_speed:
            self._current_speed == self._top_speed
        else:
            self._current_speed += ((self._top_speed) * (self._acceleration_factor))

    def decelerate(self):
        if self._current_speed <(int(self._top_speed)) * (int(self._acceleration_factor)):
             return self._current_speed == 0.0
        else:
            self._current_speed -= (int(self._top_speed)) * (int(self._acceleration_factor))
            

        

        
