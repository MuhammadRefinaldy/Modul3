import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = BukuModel()
        self.view = BukuView()

        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_delete.configure(command=self.hapus_data)
        self.view.btn_update.configure(command=self.perbarui_data)

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan isi tabel di View terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari Model (database)
        data_buku = self.model.get_all_buku()

        # Memasukkan data baru ke dalam tabel View
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def simpan_data(self):
        # Mengambil teks dari kotak input di View
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        # Validasi Form Kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        # Mengirim data ke Model untuk disimpan
        berhasil = self.model.create_buku(judul, penulis, tahun)

        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            # Bersihkan form
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')

            # Muat ulang tabel agar data terbaru muncul
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")
            
    def hapus_data(self):
        # Mengambil baris yang dipilih
        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan", "Pilih data buku yang ingin dihapus!"
            )
            return

        # Mengambil id_buku dari kolom pertama
        item = self.view.tabel.item(pilihan[0])
        id_buku = item['values'][0]

        konfirmasi = messagebox.askyesno(
            "Konfirmasi", "Apakah Anda yakin ingin menghapus data buku?"
        )

        if konfirmasi:
            berhasil = self.model.delete_buku(id_buku)

            if berhasil:
                messagebox.showinfo(
                    "Sukses", "Data buku berhasil dihapus!"
                )
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Error", "Data buku gagal dihapus."
                )

    def perbarui_data(self):
        # Mengambil baris yang dipilih
        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan", "Pilih data buku yang ingin diperbarui!"
            )
            return

        # Mengambil id_buku dari tabel
        item = self.view.tabel.item(pilihan[0])
        id_buku = item['values'][0]

        # Mengambil data dari form
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan", "Semua kolom form harus diisi!"
            )
            return

        # Mengirim perubahan ke Model
        berhasil = self.model.update_buku(
            id_buku, judul, penulis, tahun
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses", "Data buku berhasil diperbarui!"
            )

            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')

            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error", "Data buku gagal diperbarui."
            )

    # Fungsi untuk menyalakan aplikasi
    def run(self):
        self.view.mainloop()