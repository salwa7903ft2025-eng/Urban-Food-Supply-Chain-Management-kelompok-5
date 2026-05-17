import time
from dataclasses import dataclass

from modules.graph_rantai_pasok import GraphRantaiPasok
from modules.circular_queue_buffer_gudang import CircularQueue
from modules.priority_queue_pengiriman import PriorityQueueKirim
from modules.bst_katalog_produk import BSTKatalog
from modules.dijkstra_biaya_minimum import dijkstra_biaya, rekonstruksi_jalur

@dataclass
class Produk:
    kode: str
    nama: str
    kategori: str
    harga_satuan: float
    stok: int
    masa_kadaluarsa_hari: int


@dataclass
class Pengiriman:
    pengiriman_id: int
    dari_node: str
    ke_node: str
    kode_produk: str
    jumlah: int
    prioritas: int
    waktu_kirim: float


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        data = self.top.data
        self.top = self.top.next
        return data


class SupplyChainCLI:
    def __init__(self):
        self.graph = GraphRantaiPasok()
        self.bst = BSTKatalog()
        self.pq = PriorityQueueKirim()
        self.log = Stack()
        self.buffer = {}
        self.counter = 1

    def tambah_node_awal(self):
        data_node = [
            ('PTN01', 'PETANI'),
            ('DST01', 'DISTRIBUTOR'),
            ('PSR01', 'PASAR'),
            ('GDG01', 'GUDANG')
        ]

        for node, tipe in data_node:
            self.graph.tambah_node(node, tipe)
            self.buffer[node] = CircularQueue(50)

        self.graph.tambah_jalur('PTN01', 'DST01', 20, 3000)
        self.graph.tambah_jalur('DST01', 'PSR01', 15, 2500)
        self.graph.tambah_jalur('DST01', 'GDG01', 10, 2000)

    def tambah_produk_awal(self):
        data_produk = [
            Produk('PRD-001', 'Beras', 'BAHAN_POKOK', 15000, 100, 30),
            Produk('PRD-002', 'Cabai', 'SAYUR', 40000, 50, 3),
            Produk('PRD-003', 'Tomat', 'SAYUR', 10000, 70, 5)
        ]

        for produk in data_produk:
            self.bst.insert(produk)

    def kirim_produk(self, dari, ke, kode, jumlah):
        produk = self.bst.search(kode)

        if produk is None:
            print('Produk tidak ditemukan')
            return

        if produk.stok < jumlah:
            print('Stok tidak cukup')
            return

        prioritas = 1 if produk.masa_kadaluarsa_hari <= 3 else 2

        pengiriman = Pengiriman(
            self.counter,
            dari,
            ke,
            kode,
            jumlah,
            prioritas,
            time.time()
        )

        self.pq.enqueue(pengiriman)
        self.counter += 1

        print('Pengiriman masuk antrian')

    def proses_pengiriman(self):
        data = self.pq.dequeue()

        if data is None:
            print('Antrian kosong')
            return

        produk = self.bst.search(data.kode_produk)

        if produk:
            produk.stok -= data.jumlah
            self.buffer[data.ke_node].enqueue(produk.nama)
            self.log.push(data)

        print(f'Pengiriman {data.pengiriman_id} diproses')

    def cek_stok(self, kode):
        produk = self.bst.search(kode)

        if produk:
            print(vars(produk))
        else:
            print('Produk tidak ditemukan')

    def rute_murah(self, asal, tujuan):
        dist, parent = dijkstra_biaya(self.graph, asal)
        path = rekonstruksi_jalur(parent, tujuan)

        print(' -> '.join(path))
        print(f'Total biaya: {dist[tujuan]}')

    def produk_kadaluarsa(self, maks_hari):
        hasil = self.bst.filter_kadaluarsa(maks_hari)

        for item in hasil:
            print(vars(item))

    def laporan_distribusi(self):
        top = self.log.top

        while top:
            data = top.data
            print(
                f'{data.pengiriman_id} | '
                f'{data.kode_produk} | '
                f'{data.dari_node} -> {data.ke_node}'
            )
            top = top.next

    def run(self):
        self.tambah_node_awal()
        self.tambah_produk_awal()

        print('Food Supply Chain System')
        print('Ketik BANTUAN untuk melihat perintah')

        while True:
            cmd = input('>> ').split()

            if not cmd:
                continue

            if cmd[0] == 'BANTUAN':
                print('KIRIM <dari> <ke> <kode> <jumlah>')
                print('PROSES_KIRIM')
                print('RUTE_MURAH <dari> <ke>')
                print('CEK_STOK <kode>')
                print('KADALUARSA <maks_hari>')
                print('LAPORAN_DISTRIBUSI')
                print('KELUAR')

            elif cmd[0] == 'KIRIM':
                self.kirim_produk(
                    cmd[1],
                    cmd[2],
                    cmd[3],
                    int(cmd[4])
                )

            elif cmd[0] == 'PROSES_KIRIM':
                self.proses_pengiriman()

            elif cmd[0] == 'RUTE_MURAH':
                self.rute_murah(cmd[1], cmd[2])

            elif cmd[0] == 'CEK_STOK':
                self.cek_stok(cmd[1])

            elif cmd[0] == 'KADALUARSA':
                self.produk_kadaluarsa(int(cmd[1]))

            elif cmd[0] == 'LAPORAN_DISTRIBUSI':
                self.laporan_distribusi()

            elif cmd[0] == 'KELUAR':
                print('Program selesai')
                break

            else:
                print('Perintah tidak dikenali')


if __name__ == '__main__':
    app = SupplyChainCLI()
    app.run()