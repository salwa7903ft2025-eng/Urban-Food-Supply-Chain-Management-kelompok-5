import sys
import os
from dataclasses import dataclass

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../src')
    )
)

from modules.priority_queue_pengiriman import PriorityQueueKirim

@dataclass
class Pengiriman:
    pengiriman_id: int
    prioritas: int
    kode_produk: str

pq = PriorityQueueKirim()

pq.enqueue(Pengiriman(1, 2, 'PRD-001'))
pq.enqueue(Pengiriman(2, 1, 'PRD-002'))
pq.enqueue(Pengiriman(3, 3, 'PRD-003'))

pq.tampilkan_antrian()

print('\nDiproses:')
print(pq.dequeue())