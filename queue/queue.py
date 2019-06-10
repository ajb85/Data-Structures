# Queue as an array
# class Queue:
#   def __init__(self):
#     self.size = 0
#     # what data structure should we
#     # use to store queue elements?
#     self.storage = []

#   def enqueue(self, item):
#     self.storage.insert(0, item)
#     self.size += 1
  
#   def dequeue(self):
#     if(self.size > 0):
#       self.storage.pop()
#       self.size -= 1

#   def len(self):
#     return len(self.storage)
#     return self.size



# Queue as a Linked List
class Node:
  def __init__(self, value=None, nextNode=None, prevNode=None):
    self.value = value
    self.nextNode = nextNode
    self.prevNode = prevNode

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.head = None
    self.tail = None

  def enqueue(self, item):
    enqueued = Node(item, self.head)
    self.size += 1
    if(self.head == None):
      self.head = enqueued
      self.tail = enqueued
    else:
      self.head.prevNode = enqueued
      self.head = enqueued

  def dequeue(self):
    if(self.size > 0):
      value = self.tail.value
      self.tail = self.tail.prevNode
      if(self.tail != None):
        self.tail.nextNode = None
      else:
        self.head = None
      self.size -= 1
      return value
    return None
    

  def len(self):
    # return self.size
    if(self.head == None):
      return 0
    else:
      return self._countSize(self.head)

  def _countSize(self, node):
    if(node.nextNode == None):
      return 1
    return 1  + self._countSize(node.nextNode)
