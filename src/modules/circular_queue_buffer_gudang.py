class CircularQueueBuffer:
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = -1
        self.tail = -1

    def is_full(self):
        """Big-O: O(1)"""
        return (self.tail + 1) % self.capacity == self.head

    def is_empty(self):
        """Big-O: O(1)"""
        return self.head == -1

    def enqueue(self, item):
        """
        Memasukkan produk ke buffer gudang.
        Big-O: O(1)
        """
        if self.is_full():
            return False
        
        if self.head == -1:
            self.head = 0
            
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = item
        return True

    def dequeue(self):
        """
        Mengeluarkan produk dari buffer gudang (FIFO).
        Big-O: O(1)
        """
        if self.is_empty():
            return None
            
        item = self.queue[self.head]
        self.queue[self.head] = None
        
        if self.head == self.tail: # Reset jika queue kosong
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
            
        return item