class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      #go to left and add if nothing there
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        #keep going
        self.left.insert(value)
    #go to right and add it
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        #keep going
        self.right.insert(value)

  def contains(self, target):
    #return true if current value is the target
    if self.value == target:
      return True
    #if it's less, go down the left 
    if target < self.value:
      #if we cant go left, it's not there
      if not self.left:
        return False
      else: 
        return self.left.contains(target)
    #go down right otherwise
    else: 
      #if cant go right, it's not there
      if not self.right:
        return False
      else: return self.right.contains(target)

  def get_max(self):
    #return none if nothing in the tree
    if not self:
      return None
    #go down right
    #if we can't, return the current value
    if not self.right:
      return self.value
    #otherwise we keep going
    else: 
      return self.right.get_max()

  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)