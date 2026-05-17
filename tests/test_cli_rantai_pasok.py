import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../src')
    )
)

from modules.cli_rantai_pasok import SupplyChainCLI

app = SupplyChainCLI()

app.tambah_node_awal()
app.tambah_produk_awal()

app.cek_stok('PRD-001')

app.kirim_produk(
    'PTN01',
    'DST01',
    'PRD-001',
    10
)

app.proses_pengiriman()

app.laporan_distribusi()