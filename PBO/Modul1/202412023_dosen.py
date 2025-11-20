class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} (NIDN {self.nidn}) mengajar mata kuliah {mata_kuliah}"


# Pembuatan object
dosen1 = Dosen("Dr. Andi Pratama", "12345678")
dosen2 = Dosen("Prof. Siti Rahma", "87654321")

# Pemanggilan method
print(dosen1.ajar_mata_kuliah("Basis Data"))
print(dosen2.ajar_mata_kuliah("Algoritma dan Struktur Data"))
