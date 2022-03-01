class Tree:
  #constructor
  def __init__(self, initval=None):
    self.value = initval
    if self.value:
      self.left = Tree()
      self.right = Tree()
    else:
      self.left = self.right = None
    return
  
  #Only empty node has value None
  def isempty(self):
  	return(self.value == None)
  #Leaf nodes have both children empty
  def isleaf(self):
    return(self.value != None and self.left.isempty() and self.right.isempty())
  def io(self):
		if self.isempty():
			return
		else :
			return (io(self.left)+[self.value]+io(self.right))
	def __str__(self):
    return (str(self.inorder()))

#insert element to BST
def insertToBST(root, x):
  # Tree should have atleast one element.
  temp = root
  while (not temp.isempty()):
    if (x < temp.value):
      temp = temp.left
    else:
      temp = temp.right

  temp.value = x
  temp.left = Tree()
  temp.right = Tree()


L = [int(item) for item in input().split(" ")]
x = int(input())
root = Tree(L[0])
for item in L[1:]:
  insertToBST(root, item)
print(root)
