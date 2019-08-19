class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []
    #use an array!

  def enqueue(self, item):
    #add an item to the back of the queue
    self.size += 1
    self.storage.append(item)
  
  def dequeue(self):
    #remove and return item from front of queue
    #check if queue is populated
    if len(self.storage) is not 0:
      self.size -= 1
      return self.storage.pop(0)

  def len(self):
    return len(self.storage)
