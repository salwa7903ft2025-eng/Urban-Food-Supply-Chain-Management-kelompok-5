from .linked_list import LLNode

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):

        node = LLNode(data)
        node.next = self.top
        self.top = node

        self.size += 1

    def pop(self):

        if not self.top:
            return None

        node = self.top
        self.top = node.next
        self.size -= 1

        return node.data

    def peek(self):

        if self.top:
            return self.top.data
