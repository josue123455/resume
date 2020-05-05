#Josue Andaluz
#final lab
#190250
#worked with Kamerie, faith and tutor


from Node import Node

class LinkedLinkedPQ:
  def _index(self, list, i):
    node = list
    for x in range(i): node = node.get_next()
    return node.get_element()

  def _set(self, list, i, item):
    node = list
    for x in range(i): node = node.get_next()
    node.set_element(item)

  def _append(self, list, item):
    tail = list
    if tail != None:
      while tail.get_next() != None:
        tail = tail.get_next()
    node = Node(item)
    if tail != None:
      tail.set_next(node)
    else:
      list = node
    return list

  def _len(self, list):
    length = 0
    node = list
    while node != None:
      length += 1
      node = node.get_next()
    return length

  def _pop(self, list):
    beforeTail = None
    tail = list
    while tail.get_next() != None:
      beforeTail = tail
      tail = tail.get_next()
    if beforeTail != None:
      beforeTail.set_next(None)
    else:
      list = None
    return (list, tail.get_element())

  def __init__(self):
    self._data = None
    self._length = 0

  def add(self, key, value):
    dataLen = self._len(self._data)
    if key >= dataLen:
      for x in range(key - dataLen + 1):
        self._data = self._append(self._data, None)
    self._set(self._data, key, self._append(self._index(self._data, key), value))
    self._length += 1

  def _findLowest(self):
    i = 0
    node = self._data
    while node != None:
      if node.get_element() != None:
        return i
      node = node.get_next()
      i += 1
    raise Error('Priority queue is empty.')

  def min(self):
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    index = self._findLowest()
    return (index, self._index(self._index(self._data, index), 0))

  def remove_min(self):
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    self._length -= 1
    n = self._data
    while n != None:
      n2 = n.get_element()
      while n2 != None:
        n2 = n2.get_next()
      n = n.get_next()
    index = self._findLowest()
    (newList, item) = self._pop(self._index(self._data, index))
    self._set(self._data, index, newList)
    return (index, item)

  def is_empty(self):
    return len(self) == 0

  def __len__(self):
    return self._length
