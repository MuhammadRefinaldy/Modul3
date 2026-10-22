from models.anggota_model import AnggotaModel

model = AnggotaModel()

#1 Menguji fungsi Create (menambah anggota baru)
print("Menambahkan data anggota...")
model.create_anggota("Alex Bhizer", "Jl. Sin City")
model.create_anggota("Budi Setiawan", "Jl. Yang Baik")
print("Data anggota berhasil disimpan ke Laragon MySQL!")

#2 Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Anggota ===")
daftar_anggota = model.get_all_anggota()
for anggota in daftar_anggota:
    print(f"[{anggota['id_anggota']}]{anggota['nama']} - {anggota['alamat']}")