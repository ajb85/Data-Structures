class Heap:
  def __init__(self):
    self.storage = []
    self.index = 0
    
  def comparator(self, x, y):
    return x > y

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    length = len(self.storage)
    if(length == 0):
      return None
    value = self.storage[0]
    if(length > 1):
      self.storage[0] = self.storage.pop()
      self._sift_down(0)
    else:
      self.storage.pop()
    return value

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if(index == None or index <= 0):
      return None
    pIndex = round(index/2 - 1) if index % 2 == 0 else round(index/2 - 0.5)
    self._bubble_up(self._compare_and_swap_nodes(pIndex, index, "child"))

  def _sift_down(self, index):
    if(index == None):
      return None
    left = 2*index + 1
    right = 2*index + 2
    if(left > len(self.storage)-1):
      return None
    elif(right > len(self.storage)-1):
      cIndex = left
    else:
      cIndex = left if self.comparator(self.storage[left], self.storage[right]) else right

    self._sift_down(self._compare_and_swap_nodes(index, cIndex))

  def _compare_and_swap_nodes(self, pIndex, cIndex, node="parent"):
    if(self.storage[cIndex] == self.storage[pIndex]):
      return None    
    isInOrder = self.comparator(self.storage[pIndex], self.storage[cIndex])
    if(not isInOrder):
      self.storage[pIndex], self.storage[cIndex] = self.storage[cIndex], self.storage[pIndex]
      return cIndex if node=="parent" else pIndex
    return None
