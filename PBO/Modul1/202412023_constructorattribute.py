class buku:
    #attribute
    perpustakaan = "Perpustakaan STITEK"
    
    #constructor
    def __init__(self, judul, penulis, tahun):
         #Instance attributes
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        
    def info_buku(self):
        return f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun: {self.tahun}"
    
    #instansiasi objek
buku1=buku("Pemrograman Python", "Andi Pratama", 2020)
buku2=buku("Data Science", "Siti Rahma", 2021)
    
print(buku1.info_buku())
print(buku2.info_buku())
print(f"Perpustakaan: {buku.perpustakaan}")