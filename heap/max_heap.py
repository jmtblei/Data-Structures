class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # Check if storage is empty, if it is start at beginning
    # Put the value at the end of the list (append)
    # if Arr[i] > Arr[i/2] then swap (parent is bigger)
    self.storage.append(value)
    current_index = self.get_size() - 1
    self._bubble_up(current_index)
    # print(len(self.storage))

  def delete(self):
    # delete(): Deleting a key also takes O(Logn) time. We replace the 
    # key to be deleted with minum infinite by calling decreaseKey(). 
    # After decreaseKey(), the minus infinite value must reach root, 
    # so we call extractMin() to remove the key.
    last_index = self.get_size() - 1
    self.storage[0], self.storage[last_index] = self.storage[last_index], self.storage[0]
    deleted = self.storage.pop()
    # print('deleted')
    self._sift_down(0)
    return deleted

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass
