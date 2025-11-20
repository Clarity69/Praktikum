class mahasiswa:
    def __init__(self, nama, nim,):
        self.nama = nama
        self.nim = nim
    
    def perkenalan(self):
        return f"Nama saya {self.nama}, NIM saya {self.nim}"
    
#Objek
mhs1 = mahasiswa("Taro", "202412023")
mhs2 = mahasiswa("Budi", "202412024")

print(mhs1.perkenalan())
print(mhs2.perkenalan())