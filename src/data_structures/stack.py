class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        return self.top.data if self.top else None
