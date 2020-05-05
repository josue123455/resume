#Josue Andaluz
#190250
#lab 4
from Double_Node import DNode


class BinaryNode(DNode):
    
    def __init__(self, element = None, parent = None, left = None, right = None):
        super().__init__(element, left, right)
        self._parent = parent
        

    def get_element(self):
        return self._element
    

    def get_parent(self):
        return self._parent

    
    def get_left(self):
        return self._prev


    def get_right(self):
        return self._next



    #------------------------------mutators-------------------------------



    #super.set_element()


    def set_parent(self, new_parent):
        old_parent = self._parent
        self._parent = new_parent
        return old_parent



    
    def set_right(self, new_right):
        super().set_next(new_right)


                       
    def set_left(self, new_left):
        super().set_previous(new_left)
        

    

    

    

