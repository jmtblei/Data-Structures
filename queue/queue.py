from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = DoublyLinkedList()

  def enqueue(self, item):
    #add an item to the back of the queue
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    #remove and return item from front of queue
    #check if queue is populated
    if self.size > 0:
      self.size -= 1
    else:
      return None
      
    return self.storage.remove_from_head()

  def len(self):
    return self.size