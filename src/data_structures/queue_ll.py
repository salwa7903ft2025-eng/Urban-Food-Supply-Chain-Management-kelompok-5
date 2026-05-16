class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        temp = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return temp.data
