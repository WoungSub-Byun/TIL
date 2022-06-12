class Solution:

    def __init__(self):
        self.stack = []
        self.TOP = -1

    def pop(self):
        del self.stack[self.TOP]
        self.TOP -= 1
        return self.stack

    def push(self, item):
        self.TOP += 1
        self.stack.insert(self.TOP, item)
        return self.stack

    def peek(self):
        return self.stack[self.TOP]

    def isEmpty(self):
        return self.TOP == -1 and True or False
