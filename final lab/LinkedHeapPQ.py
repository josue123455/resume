#Josue Andaluz
#final lab
#190250
#worked with kamerrie, faith, and tutor
from Double_Node import DNode
class LinkedHeapPQ:
  def _index(self, i):
    node = self._data
    for x in range(i): node = node.get_next()
    return node.get_element()

  def _set(self, i, item):
    node = self._data
    for x in range(i): node = node.get_next()
    node.set_element(item)

  def _append(self, item):
    node = DNode(item, self._tail, None)
    if self._tail != None:
      self._tail.set_next(node)
    else:
      self._data = node
    self._tail = node
    self._length += 1

  def _pop(self):
    node = self._tail
    self._tail = node.get_previous()
    if self._tail == None:
      self._data = None
    self._length -= 1
    return node.get_element()

  def _parent(self, j):
    return (j-1) // 2

  def _left(self, j):
    return 2*j + 1
  
  def _right(self, j):
    return 2*j + 2

  def _has_left(self, j):
    return self._left(j) < self._length     
  
  def _has_right(self, j):
    return self._right(j) < self._length    
  
  def _swap(self, i, j):
    
    tmp = self._index(j)
    self._set(j, self._index(i))
    self._set(i, tmp)

  def _upheap(self, j):
    parent = self._parent(j)
    if j > 0 and self._index(j) < self._index(parent):
      self._swap(j, parent)
      self._upheap(parent)             
  
  def _downheap(self, j):
    if self._has_left(j):
      left = self._left(j)
      small_child = left               
      if self._has_right(j):
        right = self._right(j)
        if self._index(right) < self._index(left):
          small_child = right
      if self._index(small_child) < self._index(j):
        self._swap(j, small_child)
        self._downheap(small_child)    

  #------------------------------ public behaviors ------------------------------
  def __init__(self):
    
    self._data = None
    self._tail = None
    self._length = 0

  def is_empty(self):                  
    
    return len(self) == 0

  def __len__(self):
    
    return self._length

  def add(self, key, value):
    
    self._append((key, value))
    self._upheap(self._length - 1)            
  
  def min(self):
    

    
    
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    item = self._index(0)
    return item

  def remove_min(self):
    
    
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    self._swap(0, self._length - 1)           
    item = self._pop()                      
    self._downheap(0)                            
    return item


