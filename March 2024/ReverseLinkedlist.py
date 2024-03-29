'''
Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?

Example:
Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        node = self
        output = '' 
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution
    def reverseIteratively(self, head):
        prev = None
        current = head
        while current != None:
            temp = current.next  
            current.next = prev  
            prev = current  
            current = temp  
        return prev  

    # Recursive Solution      
    def reverseRecursively(self, head):
        if not head or not head.next:
            return head

        new_head = self.reverseRecursively(head.next)

        head.next.next = head
        head.next = None

        return new_head
        

# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
#testHead.reverseIteratively(testHead)
testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4
