from .node import Node  

class Stack:
    def __init__(self):
        self.top = None  

    def is_empty(self):python tests/test_stack.py

        return self.top is None  

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None  
        
        # PERBAIKAN: Cek node.py lu pake .data atau .item? Umumnya .data
        popped_item = self.top.data  
        self.top = self.top.next
        return popped_item
