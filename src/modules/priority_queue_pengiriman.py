class NodePQ:
    def __init__(self, data):
        self.data = data
        self.next = None


class PriorityQueueKirim:
    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, pengiriman):
        new_node = NodePQ(pengiriman)

        if self.head is None:
            self.head = new_node

        elif pengiriman.prioritas < self.head.data.prioritas:
            new_node.next = self.head
            self.head = new_node

        else:
            curr = self.head

            while (
                curr.next and
                curr.next.data.prioritas <= pengiriman.prioritas
            ):
                curr = curr.next

            new_node.next = curr.next
            curr.next = new_node

        self._size += 1

    def dequeue(self):
        if self.head is None:
            return None

        removed = self.head.data
        self.head = self.head.next
        self._size -= 1

        return removed

    def peek(self):
        if self.head:
            return self.head.data
        return None

    def tampilkan_antrian(self):
        curr = self.head

        while curr:
            data = curr.data
            print(
                f'{data.pengiriman_id} | '
                f'{data.kode_produk} | '
                f'Prioritas {data.prioritas}'
            )
            curr = curr.next

    def __len__(self):
        return self._size