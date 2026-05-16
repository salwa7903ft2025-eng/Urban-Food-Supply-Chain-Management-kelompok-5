# NEXT TIME
import time

from priority_queue import PriorityQueueKirim, Pengiriman
from dijkstra_module import (
    dijkstra_biaya,
    rekonstruksi_jalur,
    merge_sort_biaya
)


class CLIRantaiPasok:

    def __init__(
        self,
        graph,
        bst_katalog,
        pq_kirim,
        buffer_gudang
    ):

        self.graph = graph
        self.bst_katalog = bst_katalog
        self.pq_kirim = pq_kirim
        self.buffer_gudang = buffer_gudang

        self.kirim_counter = 1
        self.audit_distribusi = []

    # ==========================================
    # KIRIM
    # ==========================================

    def command_kirim(self, args):

        if len(args) != 4:
            print("Format:")
            print("KIRIM <dari> <ke> <kode> <jumlah>")
            return

        dari, ke, kode, jumlah = args

        jumlah = int(jumlah)

        produk = self.bst_katalog.search(kode)

        if produk is None:
            print("Produk tidak ditemukan")
            return

        if produk.stok < jumlah:
            print("Stok tidak mencukupi")
            return

        # menentukan prioritas
        hari = produk.masa_kadaluarsa_hari

        if hari <= 3:
            prioritas = 1
        elif hari <= 7:
            prioritas = 2
        else:
            prioritas = 3

        pengiriman = Pengiriman(
            pengiriman_id=self.kirim_counter,
            dari_node=dari,
            ke_node=ke,
            kode_produk=kode,
            jumlah=jumlah,
            prioritas=prioritas,
            waktu_kirim=time.time()
        )

        self.pq_kirim.enqueue(pengiriman)

        self.kirim_counter += 1

        print("Pengiriman masuk queue")

    # ==========================================
    # PROSES KIRIM
    # ==========================================

    def command_proses_kirim(self):

        pengiriman = self.pq_kirim.dequeue()

        if pengiriman is None:
            print("Tidak ada pengiriman")
            return

        # update stok
        self.bst_katalog.update_stok(
            pengiriman.kode_produk,
            -pengiriman.jumlah
        )

        # cari rute murah
        dist, parent = dijkstra_biaya(
            self.graph,
            pengiriman.dari_node
        )

        total_biaya = dist[pengiriman.ke_node]

        path = rekonstruksi_jalur(
            parent,
            pengiriman.ke_node
        )

        self.audit_distribusi.append(
            (
                pengiriman.pengiriman_id,
                total_biaya
            )
        )

        print("\n=== PENGIRIMAN DIPROSES ===")

        print(f"ID           : {pengiriman.pengiriman_id}")
        print(f"Produk       : {pengiriman.kode_produk}")
        print(f"Jumlah       : {pengiriman.jumlah}")

        print(
            f"Rute         : {' -> '.join(path)}"
        )

        print(
            f"Total Biaya  : {total_biaya}"
        )

    # ==========================================
    # RUTE MURAH
    # ==========================================

    def command_rute_murah(self, args):

        if len(args) != 2:
            print("Format:")
            print("RUTE_MURAH <dari> <ke>")
            return

        asal, tujuan = args

        dist, parent = dijkstra_biaya(
            self.graph,
            asal
        )

        path = rekonstruksi_jalur(
            parent,
            tujuan
        )

        print("\n=== RUTE TERMURAH ===")

        print(
            f"Jalur : {' -> '.join(path)}"
        )

        print(
            f"Biaya : {dist[tujuan]}"
        )

    # ==========================================
    # CEK STOK
    # ==========================================

    def command_cek_stok(self, args):

        if len(args) != 1:
            print("Format:")
            print("CEK_STOK <kode>")
            return

        kode = args[0]

        produk = self.bst_katalog.search(kode)

        if produk is None:
            print("Produk tidak ditemukan")
            return

        print("\n=== DATA PRODUK ===")

        print(f"Kode       : {produk.kode}")
        print(f"Nama       : {produk.nama}")
        print(f"Kategori   : {produk.kategori}")
        print(f"Stok       : {produk.stok}")

        print(
            f"Kadaluarsa : "
            f"{produk.masa_kadaluarsa_hari} hari"
        )

    # ==========================================
    # KADALUARSA
    # ==========================================

    def command_kadaluarsa(self, args):

        if len(args) != 1:
            print("Format:")
            print("KADALUARSA <maks_hari>")
            return

        maks_hari = int(args[0])

        hasil = self.bst_katalog.filter_kadaluarsa(
            maks_hari
        )

        print("\n=== PRODUK MENDEKATI KADALUARSA ===")

        if len(hasil) == 0:
            print("Tidak ada")
            return

        for p in hasil:

            print(
                f"{p.kode} | "
                f"{p.nama} | "
                f"{p.masa_kadaluarsa_hari} hari"
            )

    # ==========================================
    # LAPORAN DISTRIBUSI
    # ==========================================

    def command_laporan(self):

        if len(self.audit_distribusi) == 0:
            print("Belum ada distribusi")
            return

        hasil_sort = merge_sort_biaya(
            self.audit_distribusi
        )

        print("\n=== LAPORAN DISTRIBUSI ===")

        for pid, biaya in hasil_sort:

            print(
                f"Pengiriman {pid} "
                f"=> Biaya {biaya}"
            )

    # ==========================================
    # BUFFER
    # ==========================================

    def command_buffer(self, args):

        if len(args) != 1:
            print("Format:")
            print("BUFFER <node>")
            return

        node = args[0]

        if node not in self.buffer_gudang:
            print("Node tidak ditemukan")
            return

        buffer = self.buffer_gudang[node]

        print("\n=== BUFFER GUDANG ===")

        print(f"Node      : {node}")
        print(f"Isi Buffer: {len(buffer)}")

    # ==========================================
    # LOOP CLI
    # ==========================================

    def run(self):

        print("=== FOOD SUPPLY CHAIN SYSTEM ===")
        print("Ketik KELUAR untuk berhenti")

        while True:

            command = input("\n>> ").strip()

            if command == "":
                continue

            parts = command.split()

            cmd = parts[0].upper()
            args = parts[1:]

            try:

                if cmd == "KIRIM":
                    self.command_kirim(args)

                elif cmd == "PROSES_KIRIM":
                    self.command_proses_kirim()

                elif cmd == "RUTE_MURAH":
                    self.command_rute_murah(args)

                elif cmd == "CEK_STOK":
                    self.command_cek_stok(args)

                elif cmd == "KADALUARSA":
                    self.command_kadaluarsa(args)

                elif cmd == "LAPORAN_DISTRIBUSI":
                    self.command_laporan()

                elif cmd == "BUFFER":
                    self.command_buffer(args)

                elif cmd == "KELUAR":

                    print("Program selesai")
                    break

                else:
                    print("Command tidak dikenal")

            except Exception as e:
                print(f"Error: {e}")
