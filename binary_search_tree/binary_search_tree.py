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
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    elif(value < self.value):
      if(self.left == None):
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)    

  def contains(self, target):
    if(target == self.value):
      return True
    leftContains = self.left.contains(target) if self.left != None else False
    rightContains = self.right.contains(target) if self.right != None else False
    return leftContains or rightContains

  def get_max(self):
    # Greater numbers to the right, always check right until None.
    if(self.right == None):
      return self.value
    return self.right.get_max()

  def for_each(self, cb):
    if(self.left != None):
      self.left.for_each(cb)
    if(self.right != None):
      self.right.for_each(cb)
    return cb(self.value)
