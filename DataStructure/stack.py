class Solution:

    stack = []

    def pop(self):
        behind_data = self.stack[-1]
        del stack[-1]
        return behind_data

    def push(self, item):
        return self.stack.insert(-1, item)

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        if len(stack) == 0:
            return True
        else:
            return False
