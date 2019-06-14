"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, next=None, prev=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    newHead = ListNode(value, self.head)
    self.length += 1
    if(self.head == None):
      self.head = newHead
      self.tail = newHead
    else:
      self.head.prev = newHead
      self.head = newHead

  def remove_from_head(self):
    if(self.head == None):
      return
    value = self.head.value
    self.head = self.head.next
    self.length -= 1
    if(self.head != None):
      self.head.prev = None
    else:
      self.tail = None
    return value

  def add_to_tail(self, value):
    newTail = ListNode(value, None, self.tail)
    self.length += 1
    if(self.tail == None):
      self.tail = newTail
      self.head = newTail
    else:
      self.tail.next = newTail
      self.tail = newTail


  def remove_from_tail(self):
    # tail is none --> return
    # tail is last item --> remove and return
    # otherwise remove and return
    if(self.tail == None):
      return
    value = self.tail.value
    self.tail = self.tail.prev
    self.length -= 1
    if(self.tail != None):
      self.tail.next = None
    else:
      self.head = None
    return value

  def move_to_front(self, node):
    # If node is head, do nothing
    # If list has no length, do nothing
    # If it's the tail, prev should be set to None
    # Else, next node's prev should be current node's prev and vice versa
      #  current node's next should be current head and prev node None
    if(node == self.head or self.length == 0):
      return
    self._extract_node_to_ends(node, "head")
    
    

  def move_to_end(self, node):
    # If node is tail or list has no length, do nothing
    # If node is head, head.next.prev is none

    if(node == self.tail or self.length == 0):
      return
    self._extract_node_to_ends(node, "tail")

  def delete(self, node):
    if(self.length == 0):
      return None
    self.length -= 1
    self._extract_node(node)
    return node.value

  def get_max(self):
    current = self.head
    max = None
    while(current != None):
      if(max == None or current.value > max):
        max = current.value
      current = current.next
    return max
    
  def _extract_node_to_ends(self, node, position):
    self._extract_node(node)
    
    old_node = getattr(self, position)
    link_new_to_old = "next" if position == "head" else "prev"
    link_old_to_new = "prev" if position == "head" else "next"
    setattr(old_node, link_old_to_new, node)

    setattr(node, link_new_to_old, old_node)
    setattr(node, link_old_to_new, None)
    setattr(self, position, node)

  def _extract_node(self,node):
    if(node == self.head and node == self.tail):
      self.head = None
      self.tail = None
      self.length = 0
    elif(node == self.head):
      node.next.prev = None
      self.head = node.next
    elif(node == self.tail):
      node.prev.next = None
      self.tail = node.prev
    else:
      node.next.prev = node.prev
      node.prev.next = node.next