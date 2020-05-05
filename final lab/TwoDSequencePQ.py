#Josue Andaluz
#final lab
#190250
#worked with Kamerie, faith and tutor
from Double_Node import DNode
class TwoDSequencePQ:
  def __init__(self):
    self._data = []
    self._length = 0

  def add(self, key, value):
    if key >= len(self._data):
      for x in range(key - len(self._data) + 1):
        self._data.append([])
    self._data[key].append(value)
    self._length += 1

  def _findLowest(self):
    for i in range(len(self._data)):
       if len(self._data[i]) > 0:
         return i
    raise Error('Priority queue is empty.')

  def min(self):
    if self.is_empty():
      raise Empty('Priority queue is empdone ty.')
    index = self._findLowest()
    return (index, self._data[index][0])

  def remove_min(self):
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    self._length -= 1
    index = self._findLowest()
    return (index, self._data[index].pop())

  def is_empty(self):
    return len(self) == 0

  def __len__(self):
    return self._length
