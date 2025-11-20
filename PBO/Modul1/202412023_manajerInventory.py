class ManajerInventori:
    def __init__(self):
        # inventori berbentuk dictionary: {nama_barang: stok}
        self.inventori = {}
        
    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong"

        daftar = "Daftar Inventori:\n"
        for barang, stok in self.inventori.items():
            daftar += f"- {barang}: {stok} unit\n"
        return daftar.strip()

    def tambah_barang(self, nama, jumlah):
        if jumlah <= 0:
            return "Jumlah harus lebih dari 0"
        if nama in self.inventori:
            self.inventori[nama] += jumlah
        else:
            self.inventori[nama] = jumlah

        return f"Berhasil menambahkan {jumlah} unit {nama}. Stok sekarang: {self.inventori[nama]}"

    def hapus_barang(self, nama, jumlah):
        if nama not in self.inventori:
            return f"{nama} tidak ditemukan dalam inventori"
        if jumlah <= 0:
            return "Jumlah harus lebih dari 0"
        if jumlah > self.inventori[nama]:
            return f"Stok {nama} tidak mencukupi"
        self.inventori[nama] -= jumlah
        if self.inventori[nama] == 0:
            del self.inventori[nama]
            return f"Semua stok {nama} habis dan barang dihapus dari inventori"

        return f"Berhasil mengurangi {jumlah} unit {nama}. Stok tersisa: {self.inventori[nama]}"


# Demonstrasi semua method
inv = ManajerInventori()

print(inv.tambah_barang("Laptop", 10))
print(inv.tambah_barang("Mouse", 25))
print(inv.tambah_barang("Laptop", 5))      # menambah stok barang yang sudah ada

print(inv.hapus_barang("Mouse", 10))
print(inv.hapus_barang("Laptop", 15))      # menghapus sebagian stok
print(inv.hapus_barang("Laptop", 0))       # error jumlah
print(inv.hapus_barang("Laptop", 100))     # stok tidak cukup

print(inv.lihat_inventori())
