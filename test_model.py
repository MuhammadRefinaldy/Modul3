from models.buku_model import BukuModel

model = BukuModel()

#1 Menguji fungsi Create (menambah buku baru)
print("Menambahkan data buku...")
model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
print("Data berhasil disimpan ke Laragon MySQL!")

#2 Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}]{buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

#3 Menguji fungsi Update (mengubah buku terakhir)
id_uji = daftar_buku[-1]['id_buku']
print(f"\nMengubah data buku ID {id_uji}...")
model.update_buku(id_uji, "Pemrograman Python MVC (Edisi Revisi)", "Guido van Rossum", 2024)
print("Data berhasil diperbarui!")

print("\n=== Daftar Buku (Setelah Update) ===")
for buku in model.get_all_buku():
    print(f"[{buku['id_buku']}]{buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

#4 Menguji fungsi Delete (menghapus buku yang tadi diubah)
print(f"\nMenghapus data buku ID {id_uji}...")
model.delete_buku(id_uji)
print("Data berhasil dihapus!")

print("\n=== Daftar Buku (Setelah Delete) ===")
for buku in model.get_all_buku():
    print(f"[{buku['id_buku']}]{buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")