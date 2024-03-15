'''
You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        current = result
        carry = 0

        # Mientras haya algo que sumar
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)

            total = val1 + val2 + carry
            carry = total // 10
            sum = total % 10

            current.next = ListNode(sum)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return result.next
    
if __name__ == '__main__':
    
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)

    while result:
        print(result.val),
        result = result.next
    # 7 0 8
  




