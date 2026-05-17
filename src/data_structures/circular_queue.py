class CircularQueue:
    def __init__(self, kapasitas=50):
        self.kapasitas = kapasitas
        self.buffer = [None] * kapasitas
        self.front = 0
        self.rear = 0
        self.size = 0

    # Big-O: O(1)
    def enqueue(self, data):
        if self.is_full():
            return False

        self.buffer[self.rear] = data
        self.rear = (self.rear + 1) % self.kapasitas
        self.size += 1

        return True

    # Big-O: O(1)
    def dequeue(self):
        if self.is_empty():
            return None

        data = self.buffer[self.front]

        self.buffer[self.front] = None
        self.front = (self.front + 1) % self.kapasitas

        self.size -= 1

        return data

    # Big-O: O(1)
    def peek(self):
        if self.is_empty():
            return None

        return self.buffer[self.front]

    # Big-O: O(1)
    def is_empty(self):
        return self.size == 0

    # Big-O: O(1)
    def is_full(self):
        return self.size == self.kapasitas

    # Big-O: O(n)
    def display(self):
        if self.is_empty():
            print("Buffer kosong")
            return

        idx = self.front

        for _ in range(self.size):
            print(self.buffer[idx])
            idx = (idx + 1) % self.kapasitas

    # Big-O: O(1)
    def __len__(self):
        return self.size