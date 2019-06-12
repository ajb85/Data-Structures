class Heap:
  def __init__(self):
    self.storage = []
    self.index = 0
    
  def comparator(self, x, y):
    return x > y

  def insert(self, value):
    self.storage.append(value)
    index = len(self.storage) - 1
    while(index != None):
      index = self._bubble_up(index)
    

  def delete(self):
    value = self.storage[0]
    self.storage[0] = self.storage.pop()
    index = 0
    while index != None:
      index = _sift_down(self.storage[index])

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if(index <= 0):
      return None
    pIndex = round(index/2 - 1) if index % 2 == 0 else round(index/2 - 0.5)
    return self._compare_and_swap_nodes(pIndex, index)

  def _sift_down(self, index):
    left = 2*index + 1
    right = 2*index + 2
    if(left > len(self.storage)-1):
      return None
    elif(right > len(self.storage)-1):
      cIndex = left
    else:
      cIndex = left if self.comparator(self.storage[left], self.storage[right]) else right
    return self._compare_and_swap_nodes(index, cIndex)

  def _compare_and_swap_nodes(pIndex, cIndex):
    isInOrder = self.comparator(self.storage[pIndex], self.storage[cIndex])
    if(not isInOrder):
      self.storage[pIndex], self.storage[cIndex] = self.storage[cIndex], self.storage[pIndex]
      return cIndex
    return None



  def _get_children(self, index):
    return {"left": 2*index + 1, "right": 2*index + 2}
