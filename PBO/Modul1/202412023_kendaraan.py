class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        # Instance attributes
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"{self.merk} warna {self.warna}, tahun {self.tahun}"


# Instansiasi object
kendaraan1 = Kendaraan("Yamaha NMAX", "Hitam", 2021)
kendaraan2 = Kendaraan("Honda Supra", "Merah", 2019)

# Akses instance attribute
print(kendaraan1.info_kendaraan())
print(kendaraan2.info_kendaraan())

# Akses class attribute
print(f"Bahan bakar (akses via class): {Kendaraan.bahan_bakar}")
print(f"Bahan bakar (akses via objek 1): {kendaraan1.bahan_bakar}")
print(f"Bahan bakar (akses via objek 2): {kendaraan2.bahan_bakar}")
