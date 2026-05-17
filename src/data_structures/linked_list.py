from typing import Optional, Any

class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional['Node'] = None

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete(self, key: Any) -> bool:
        if self.head is None:
            return False

        if self.head.data == key:
            self.head = self.head.next
            return True

        current = self.head
        while current.next is not None:
            if current.next.data == key:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def display(self) -> None:
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

        #lha ? g kedetect changes nya ??????