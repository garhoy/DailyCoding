'''
You are given the root of a binary tree. Invert the binary tree in place. That is, all left children should become right children, and all right children should become left children.

Example:

    a
   / \
  b   c
 / \  /
d   e f

The inverted version of this tree is as follows:

  a
 / \
 c  b
 \  / \
  f e  d

  '''
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def preorder(self):
        print(self.value, end=" ")
        if self.left: 
            self.left.preorder()
        if self.right: 
            self.right.preorder()

    def invert(self):
        self.left, self.right = self.right, self.left
        
        if self.left: 
            self.left.invert()
        if self.right: 
            self.right.invert()

root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 


print("Preorder traversal before inversion:")
root.preorder()

root.invert()

print("\n\nPreorder traversal after inversion:")
root.preorder()
