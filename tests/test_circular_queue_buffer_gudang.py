import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../src')
    )
)

from modules.circular_queue_buffer_gudang import CircularQueue

queue = CircularQueue(3)

queue.enqueue('Beras')
queue.enqueue('Cabai')
queue.enqueue('Tomat')

print(queue.dequeue())
print(queue.dequeue())

queue.enqueue('Ayam')

queue.tampilkan_buffer()