'''
Implement a class for a stack that supports all the regular functions (push, pop) and an additional 
function of max() which returns the maximum element in the stack (return None if the stack is empty). Each method should run in constant time.
'''
class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, val):
        self.stack.append(val)

        if not self.maxStack or val > self.maxStack[-1]:
            self.maxStack.append(val)
        else:
            self.maxStack.append(self.maxStack[-1])

    def pop(self):
        if self.stack:
            self.maxStack.pop()
            return self.stack.pop()
        return None

    def max(self):
        if self.maxStack:
            return self.maxStack[-1]
        return None

# Probando la implementación
s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
