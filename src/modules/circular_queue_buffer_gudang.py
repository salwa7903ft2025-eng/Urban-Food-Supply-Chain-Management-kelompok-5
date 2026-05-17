class CircularQueue:
    def __init__(self, kapasitas=50):
        self.kapasitas = kapasitas
        self.buffer = [None] * kapasitas
        self.front = 0
        self.rear = 0
        self._size = 0

    def enqueue(self, produk):
        if self.is_full():
            return False

        self.buffer[self.rear] = produk
        self.rear = (self.rear + 1) % self.kapasitas
        self._size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None

        data = self.buffer[self.front]
        self.buffer[self.front] = None
        self.front = (self.front + 1) % self.kapasitas
        self._size -= 1

        return data

    def peek(self):
        if self.is_empty():
            return None

        return self.buffer[self.front]

    def is_full(self):
        return self._size == self.kapasitas

    def is_empty(self):
        return self._size == 0

    def tampilkan_buffer(self):
        if self.is_empty():
            print('Buffer kosong')
            return

        idx = self.front
        for _ in range(self._size):
            print(self.buffer[idx])
            idx = (idx + 1) % self.kapasitas

    def __len__(self):
        return self._size
