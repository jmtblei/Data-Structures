from doubly_linked_list import DoublyLinkedList

class LRUCache:
  def __init__(self, limit=10):
    #needs to store key value pairs (dict)
    #needs to track the order
    #needs to store cache
    #needs to store the size of cache
    self.limit = limit
    self.size = 0
    self.storage = dict()
    self.order = DoublyLinkedList
  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    if key in self.storage:
      node = self.storage[key]
      self.order.move_to_front(node)
      return node.value[1]
    else:
      return None

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    #update value and move to head if key already in cache
    if key in self.storage:
      node = self.storage(key)
      node.value = (key, value)
      self.order.move_to_front(node)
      return
    #remove the oldest (tail) if the value is at max
    if self.size == self.limit:
      del self.storage[self.order.tail.value[0]]
      self.order.remove_from_tail()
      self.size -= 1
    #add to head if pair to cache makes it the most recent
    self.order.add_to_head((key, value))
    self. storage[key] = self.order.head
    self.size += 1
