from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()

def test_get_all_buku():
    """get_all_buku() harus mengembalikan list berisi dictionary data buku."""
    model = BukuModel()

    hasil = model.get_all_buku()

    assert isinstance(hasil, list)
    for buku in hasil:
        assert {'id_buku', 'judul', 'penulis', 'tahun_terbit'} <= set(buku.keys())