class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # value is greater or less than, move right or left.  If the same, do nothing
    # When moving left or right, check for None.  If None is found, create the node
    # Else, move to next node to repeat
    if(value > self.value):
      if(self.right == None):
        # Create node
      else:
        self.right.insert(value)
    elif(value < self.value):
      if(self.right == None):
        # Create node
      else:
        self.left.insert(value)
    else:
      return
    

  def contains(self, target):
    # Value is greater or less than, move right or left.  If the same, return True
    # When moving, check for None.  If found, return False.  Else, recursion
    if(target > self.value):
      if(self.right == None):
        return False
      else:
        self.right(target)
    elif(target < self.value):
      if(self.left == None):
        return False
      else:
        self.left(target)
    else:
      return True


  def get_max(self):
    # Greater numbers to the right, always check right until None.
    right = self.right
    while right != None:
      if(right.right == None):
        return self.value
      else:
        right = right.right

  def for_each(self, cb):
    if(self.left != None):
      self.left.for_each(cb)
    if(self.right != None):
      self.right.for_each(cb)
    return cb(self.value)
