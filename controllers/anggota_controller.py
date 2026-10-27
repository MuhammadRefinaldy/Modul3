import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_delete.configure(command=self.hapus_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.tabel.bind("<<TreeviewSelect>>", self.isi_form_dari_baris)

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        for anggota in self.model.get_all_anggota():
            self.view.tabel.insert("", "end", values=(
                anggota['id_anggota'], anggota['nama'], anggota['alamat']))

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, 'end')
        self.view.entry_alamat.delete(0, 'end')

    def ambil_id_terpilih(self):
        terpilih = self.view.tabel.selection()
        if not terpilih:
            messagebox.showwarning("Peringatan", "Pilih salah satu baris anggota di tabel terlebih dahulu!")
            return None
        return self.view.tabel.item(terpilih[0])['values'][0]  # id_anggota

    def isi_form_dari_baris(self, event=None):
        terpilih = self.view.tabel.selection()
        if not terpilih:
            return
        _, nama, alamat = self.view.tabel.item(terpilih[0])['values']
        self.bersihkan_form()
        self.view.entry_nama.insert(0, nama)
        self.view.entry_alamat.insert(0, alamat)

    def simpan_data(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_anggota(nama, alamat):
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def hapus_data(self):
        id_anggota = self.ambil_id_terpilih()
        if id_anggota is None:
            return

        if not messagebox.askyesno("Konfirmasi", f"Yakin ingin menghapus anggota dengan ID {id_anggota}?"):
            return

        if self.model.delete_anggota(id_anggota):
            messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    def perbarui_data(self):
        id_anggota = self.ambil_id_terpilih()
        if id_anggota is None:
            return

        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.update_anggota(id_anggota, nama, alamat):
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def run(self):
        self.view.mainloop()

if __name__ == "__main__":
    app = AnggotaController()
    app.run()