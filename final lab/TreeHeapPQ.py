#Josue Andaluz
#final lab
#190250
#worked with Kamerie, faith and tutor 
from Binary_Node import BinaryNode
#from Double_Node import DNode
class TreeHeapPQ:
  def __init__(self):
     self._head = None
     self._length = 0

  def is_empty(self):                  
    return len(self) == 0

  def __len__(self):
    return self._length

  
  def _upheap(self, j):
    parent = self._parent(j)
    if j > 0 and self._index(j) < self._index(parent):
      self._swap(j, parent)
      self._upheap(parent)             
  

  def add(self, key, value):
    """Add a key-value pair to the priority queue."""
    if self._length == 0:
      self._head = BinaryNode((key, value))
    else:
      node = self._head 
      for i in "{0:b}".format(self._length + 1)[1:]: 
        if i == "1": 
          if node.get_right() == None: 
            node.set_right(BinaryNode((key, value), node)) 
          node = node.get_right() 
        else: 
          if node.get_left() == None: 
            node.set_left(BinaryNode((key, value), node)) 
          node = node.get_left() 
      
      while node.get_parent() != None and node.get_element()[0] < node.get_parent().get_element()[0]:
        tmp = node.get_parent().get_element()
        node.get_parent().set_element(node.get_element())
        node.set_element(tmp)
        node = node.get_parent()
    self._length += 1


  def min(self):
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    item = self._head.get_element()
    return item

  def remove_min(self):
    """Remove and return (k,v) tuple with minimum key.

    Raise Empty exception if empty.
    """
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    item = self._head.get_element()           
    if self._length == 1:
      self._head = None
      self._length -= 1
      return item
    else:
      node = self._head 
      counter = 1
      iterations = "{0:b}".format(self._length)[1:] 
      for i in iterations:
        if i == "1": 
          if counter == len(iterations):
            self._head.set_element(node.get_right().get_element())
            node.set_right(None)
          node = node.get_right() 
        else: 
          if counter == len(iterations):
            self._head.set_element(node.get_left().get_element())
            node.set_left(None)
          node = node.get_left() 
        counter += 1
    self._length -= 1
    node = self._head
    while node.get_left() != None:
      left = node.get_left()
      right = node.get_right()
      small_child = left
      if right != None:
        if right.get_element()[0] < left.get_element()[0]:
          small_child = right
      if small_child.get_element()[0] < node.get_element()[0]:
        tmp = node.get_element()
        node.set_element(small_child.get_element())
        small_child.set_element(tmp)
        node = small_child
      else:
        break
    return item

