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
    pass

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index > 0:
      parent_index = (index-1) // 2
      if self.storage[index] > self.storage[parent_index]:
        self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
      index = parent_index

  def _sift_down(self, index):
    pass
