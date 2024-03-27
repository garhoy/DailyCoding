'''
Given an integer k and a binary search tree, find ºthe floor(less than or equal to) of k 
and the ceiling(larger than or equal to) of k. If either does not exist print them as None.
'''
class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.val = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    while root_node:
        if root_node.val == k:
            floor = root_node.val
            ceil = root_node.val
            break
        elif root_node.val < k: 
            floor = root_node.val
            root_node = root_node.right
        else:  
            ceil = root_node.val
            root_node = root_node.left
    return floor, ceil

root = Node(8)
root.left = Node(4)
root.right = Node(12)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.left = Node(10)
root.right.right = Node(14)

floor, ceil = findCeilingFloor(root, 5)
print(f"Floor: {floor}, Ceil: {ceil}")
# Debería imprimir "Floor: 4, Ceil: 6"
