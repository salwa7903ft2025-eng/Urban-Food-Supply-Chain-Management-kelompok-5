import sys
import os
from dataclasses import dataclass

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from modules.bst_katalog_produk import BSTKatalog

@dataclass
class Produk:
    kode: str
    nama: str
    kategori: str
    harga_satuan: float
    stok: int
    masa_kadaluarsa_hari: int

print("CEK MODUL KATALOG")

katalog = BSTKatalog()

katalog.insert(Produk("101", "Beras Ramos", "POKOK", 15000.0, 100, 180))
katalog.insert(Produk("105", "Minyak Bimoli", "MINYAK", 18000.0, 50, 90))
katalog.insert(Produk("100", "Gula Gulaku", "POKOK", 14000.0, 200, 360))

print("Input selesai\n")

hasil = katalog.search("101")
print(f"Cari ID 101: {hasil.nama if hasil else 'Gak ketemu'}")

gaib = katalog.search("999")
print(f"Cari ID 999: {gaib}")

print("\nDaftar Katalog:")
katalog.inorder(katalog.root)