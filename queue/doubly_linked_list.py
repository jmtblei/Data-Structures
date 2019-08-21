#"""Each ListNode holds a reference to its previous node
#as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  #"""Wrap the given value in a ListNode and insert it
  #after this node. Note that this node could already
  #have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  #""Wrap the given value in a ListNode and insert it
  #before this node. Note that this node could already
  #have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  #"""Rearranges this ListNode's previous and next pointers
  #accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

#"""Our doubly-linked list class. It holds references to
#the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length
  
  #"""Wraps the given value in a ListNode and inserts it 
  #as the new head of the list. Don't forget to handle 
  #the old head node's previous pointer accordingly."""
  def add_to_head(self, value):
    new_node = ListNode(value)
    self.length += 1
    #if list is empty, the head and tail will both be the value of new_node and length will be 1
    # H <-> N <-> T
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    # AddH <-> prevH <-> N <-> T
    else:
      self.head.prev = new_node
      new_node.next = self.head
      self.head = new_node
  
  #"""Removes the List's current head node, making the
  #current head's next node the new head of the List.
  #Returns the value of the removed Node."""
  def remove_from_head(self):
    self.length -= 1
    #if list is empty, return none (can't remove what's not there!)
    if not self.head and not self.tail:
      return None
    #if list only has 1 value, head and tail are same value
    if self.head is self.tail:
      current_head = self.head
      self.head = None
      self.tail = None
      return current_head.value
    # RemoveH <-> nextH <-> N <-> T
    else:
      self.head = self.head.next
      self.head.prev = None
      return self.head.value

  #"""Wraps the given value in a ListNode and inserts it 
  #as the new tail of the list. Don't forget to handle 
  #the old tail node's next pointer accordingly."""
  def add_to_tail(self, value):
    new_node = ListNode(value)
    self.length += 1
    #same empty list check as add_to_head
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    # H <-> N <-> prevT <-> AddT
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node

  #"""Removes the List's current tail node, making the 
  #current tail's previous node the new tail of the List.
  #Returns the value of the removed Node."""
  def remove_from_tail(self):
    self.length -= 1
    #if list is empty, return none (can't remove what's not there!)
    if not self.head and not self.tail:
      return None
    #if list only has 1 value, head and tail are same value
    if self.head is self.tail:
      current_tail = self.tail
      self.head = None
      self.tail = None
      return current_tail.value
    # H <-> N <-> nextT <-> RemoveT
    else:
      self.tail = self.tail.prev
      self.tail.next = None
      return self.tail.value

  #"""Removes the input node from its current spot in the 
  #List and inserts it as the new head node of the List."""
  def move_to_front(self, node):
    #if the input node is head, the returned list will be the same
    if node is self.head:
      return
    #if input node is the tail, remove it using the function we already defined
    if node is self.tail:
      self.remove_from_tail()
    #any other value we delete temporarily
    else:
      node.delete()
      self.length -= 1
    #add removed/deleted back toe the head
    self.add_to_head(node.value)

  #"""Removes the input node from its current spot in the 
  #List and inserts it as the new tail node of the List."""
  def move_to_end(self, node):
    #if the input node is tail, the returned list will be the same
    if node is self.tail:
      return
    #if input node is the head, remove it using the function we already defined
    if node is self.head:
      self.remove_from_head()
    #any other value we delete temporarily
    else:
      node.delete()
      self.length -= 1
    #add removed/deleted back toe the head
    self.add_to_tail(node.value)

  #"""Removes a node from the list and handles cases where
  #the node was the head or the tail"""
  def delete(self, node):
    self.length -= 1
    if not self.head and not self.tail:
      return
    if self.head == self.tail:
      self.head = None
      self.tail = None
    elif self.head == node:
      self.head = node.next
      node.delete()
    elif self.tail == node:
      self.tail = node.prev
      node.delete()
    else:
      node.delete()
    
  #"""Returns the highest value currently in the list"""
  def get_max(self):
    if not self.head:
      return None
    max_val = self.head.value
    current = self.head
    while current:
      if current.value > max_val:
        max_val = current.value
      current = current.next
    return max_val
