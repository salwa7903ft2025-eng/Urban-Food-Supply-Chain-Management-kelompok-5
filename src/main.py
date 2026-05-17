import sys
from src.modules.cli_rantai_pasok import CLI
from src.modules.bst_katalog_produk import Produk
from src.modules.dijkstra_biaya_minimum import dijkstra_biaya_minimum


def setup_data_awal(cli):
    """Mengisi data awal untuk skenario uji realistis sesuai parameter sistem."""
    # 1. Setup Katalog Produk (BST)
    produk_awal = [
        Produk(101, "Beras Premium", "Pokok", 15000, 500, 180),
        Produk(102, "Cabai Merah", "Sayur", 40000, 50, 3),    # MENDESAK
        Produk(103, "Tomat Sayur", "Sayur", 12000, 80, 5),     # NORMAL
        Produk(104, "Bawang Merah", "Bumbu", 35000, 100, 14),  # REGULER
        Produk(105, "Daging Ayam", "Protein", 38000, 40, 2)    # MENDESAK
    ]
    for p in produk_awal:
        cli.katalog.insert_produk(p)

    # 2. Setup Jalur Distribusi (Graph)
    # Format: add_edge_weighted(dari, ke, jarak_km, biaya_per_km)
    jalur = [
        ("PetaniSleman", "GudangUtara", 15, 2000),
        ("PetaniBantul", "GudangSelatan", 10, 2000),
        ("GudangUtara", "DistributorA", 8, 3000),
        ("GudangSelatan", "DistributorA", 12, 3000),
        ("DistributorA", "PasarBeringharjo", 5, 5000),
        ("DistributorA", "PasarKranggan", 7, 5000)
    ]
    for j in jalur:
        # PERBAIKAN: Membongkar tuple j menggunakan indeks j[0], j[1], j[2], j[3]
        cli.graph.add_edge_weighted(j[0], j[1], j[2], j[3])

def cetak_panduan():
    print("\n" + "="*50)
    print("SISTEM MANAJEMEN RANTAI PASOK PANGAN URBAN")
    print("="*50)
    print("Perintah tersedia:")
    print("1. CEK_STOK <kode_produk>")
    print("2. KADALUARSA <maks_hari>")
    print("3. RUTE_MURAH <dari_node> <ke_node>")
    print("4. KIRIM <dari> <ke> <kode_produk> <jumlah>")
    print("5. PROSES_KIRIM")
    print("6. BUFFER <nama_node>")
    print("7. KELUAR")
    print("="*50)

def main():
    cli = CLI()
    setup_data_awal(cli)
    cetak_panduan()

    while True:
        try:
            command_input = input("\n>> Masukkan perintah: ").strip().split()
            if not command_input:
                continue

            cmd = command_input[0].upper() # PERBAIKAN: ambil elemen indeks ke-0

            if cmd == "KELUAR":
                print("Mematikan sistem... Terima kasih!")
                sys.exit(0)

            elif cmd == "CEK_STOK":
                if len(command_input) < 2:
                    print("Format salah! Gunakan: CEK_STOK <kode_produk>")
                    continue
                kode = int(command_input[1]) # PERBAIKAN: tambahkan indeks [1]
                hasil = cli.katalog.search_produk(cli.katalog.root, kode)
                if hasil:
                    print(f"Ditemukan: {hasil.data}")
                else:
                    print("Produk tidak ditemukan dalam katalog.")

            elif cmd == "KADALUARSA":
                if len(command_input) < 2:
                    print("Format salah! Gunakan: KADALUARSA <maks_hari>")
                    continue
                maks_hari = int(command_input[1]) # PERBAIKAN: tambahkan indeks [1]
                hasil = cli.katalog.filter_kadaluarsa(cli.katalog.root, maks_hari)
                print(f"Produk kadaluarsa dalam <= {maks_hari} hari:")
                for p in hasil:
                    print(f"- {p}")
                if not hasil:
                    print("Tidak ada produk yang mendekati kadaluarsa.")

            elif cmd == "RUTE_MURAH":
                if len(command_input) < 3:
                    print("Format salah! Gunakan: RUTE_MURAH <dari> <ke>")
                    continue
                dari, ke = command_input[1], command_input[2] # PERBAIKAN: tambahkan indeks [1] dan [2]
                
                if dari not in cli.graph.adj_list or ke not in cli.graph.adj_list:
                    print("Node tidak dikenali di dalam jaringan.")
                    continue

                distances, previous = dijkstra_biaya_minimum(cli.graph, dari)
                if distances[ke] == float('infinity'):
                    print(f"Tidak ada jalur dari {dari} ke {ke}.")
                else:
                    rute = []
                    curr = ke
                    while curr is not None:
                        rute.insert(0, curr)
                        curr = previous[curr]
                    print(f"Rute Termurah: {' -> '.join(rute)}")
                    print(f"Total Biaya Distribusi: Rp {distances[ke]}")

            elif cmd == "KIRIM":
                if len(command_input) < 5:
                    print("Format salah! Gunakan: KIRIM <dari> <ke> <kode> <jumlah>")
                    continue
                # PERBAIKAN: Memetakan setiap argumen input sesuai posisinya di list
                dari = command_input[1]
                ke = command_input[2]
                kode = int(command_input[3])
                jumlah = int(command_input[4])
                
                produk_node = cli.katalog.search_produk(cli.katalog.root, kode)
                if not produk_node:
                    print(f"Gagal: Produk {kode} tidak ada di katalog.")
                    continue
                
                masa_exp = produk_node.data.masa_kadaluarsa
                cli.kirim(dari, ke, kode, jumlah, masa_exp)
                produk_node.data.stok -= jumlah 

            elif cmd == "PROSES_KIRIM":
                cli.proses_kirim()

            elif cmd == "BUFFER":
                if len(command_input) < 2:
                    print("Format salah! Gunakan: BUFFER <nama_node>")
                    continue
                node = command_input[1] # PERBAIKAN: tambahkan indeks [1]
                if node not in cli.buffers or cli.buffers[node].is_empty():
                    print(f"Buffer di {node} kosong atau tidak ada.")
                else:
                    print(f"Isi Buffer {node} (FIFO):")
                    buf = cli.buffers[node]
                    idx = buf.head
                    counter = 1
                    while True:
                        item = buf.queue[idx]
                        print(f"  {counter}. Produk {item['kode']} | Qty: {item['jumlah']}")
                        if idx == buf.tail:
                            break
                        idx = (idx + 1) % buf.capacity
                        counter += 1

            else:
                print(f"Perintah '{cmd}' tidak dikenali. Ketik perintah yang valid.")

        except ValueError:
            print("Error: Pastikan input angka untuk kode produk, jumlah, dan hari valid.")
        except Exception as e:
            print(f"Terjadi kesalahan sistem: {e}")

if __name__ == "__main__":
    main()
