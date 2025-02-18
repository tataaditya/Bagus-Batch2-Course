# yeyyy sekarang saatnya praktik OOP
# ada beberapa bagian dalam OOP ingat yah
# 1. class -> nama kelas atau OOPnya
# 2. object -> Hasil dari OOPnya
# 3. attribute -> Variabel yang dimiliki OOP
# 4. method -> Kemampuan yang dimiliki oop

# contoh yah :
# class : Bintang
# object : matahari
# atribut : {warna : putih
# 	 suhu : Sangat panas
# 	 Ukuran : Kecil}
# method : Supernova, Menyala, Melakukan Fusi Nuklir


# Sekarang Time to practice
import math

# class ada code yang harus kita tuliskan diawal kalau mau membuat OOP
class Calculator:
    # atribut  __ init__ digunakan untuk
    def __init__(self):
        pass

    # kita buat 
    def penjumlahan(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2
        return self.angka1 + self.angka2
    
    def pengurangan(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2
        return self.angka1 - self.angka2
    
    def pembagian(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2
        return self.angka1 / self.angka2
    
    def perkalian(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2
        return self.angka1 * self.angka2    
    

class Scientific(Calculator):
    def __init__(self):
        super().__init__()

    def penjumlahan_sin(self, derajat1, derajat2):
        self.radiant1 = math.radians(derajat1)
        self.radiant2 = math.radians(derajat2)
        self.hasil = self.penjumlahan(math.sin(self.radiant1), math.sin(self.radiant2))
        print(f'Hasil dari sin{derajat1} + sin{derajat2} = {self.hasil}')
        
    def penjumlahan_cos(self, derajat1, derajat2):
        self.radiant1 = math.radians(derajat1)
        self.radiant2 = math.radians(derajat2)
        self.hasil = self.penjumlahan(math.cos(self.radiant1), math.cos(self.radiant2))
        print(f'Hasil dari cos{derajat1} + cos{derajat2} = {self.hasil}')

    def penjumlahan_tan(self, derajat1, derajat2):
        self.radiant1 = math.radians(derajat1)
        self.radiant2 = math.radians(derajat2)
        self.hasil = self.penjumlahan(math.tan(self.radiant1), math.tan(self.radiant2))
        print(f'Hasil dari tan{derajat1} + tan{derajat2} = {self.hasil}')

cal = Calculator()
print(cal.penjumlahan(10, 10))

sci = Scientific()
sci.penjumlahan_sin(90, 90)

# Encapsulation adalah konsep dalam OOP (Object-Oriented Programming) 
# untuk membatasi akses ke atribut dan metode dalam sebuah kelas.
# Encapsulation membantu menjaga keamanan data dan memastikan bahwa 
# hanya bagian yang seharusnya bisa diakses.

# Ada tiga jenis aksesibilitas utama:
# 1. Public
# 2. Protected
# 3. Private

# Public:
# Atribut atau metode yang bersifat public dapat diakses oleh siapa saja,
# baik dari dalam kelas, luar kelas, maupun oleh kelas turunannya.
# Contoh: `self.nama` dan `self.nim` di bawah adalah public.

# Protected:
# Atribut atau metode yang bersifat protected hanya dapat diakses oleh 
# kelas itu sendiri dan kelas turunannya (subclass). 
# Tanda protected diawali dengan satu underscore (`_`).
class Mahasiswa:
    def __init__(self, nama, nim):
        # Atribut protected
        self._nilai = 100
        # Atribut public
        self.nama = nama
        self.nim = nim

    # Metode protected
    def _hitung_nilai_akhir(self):
        # Mengubah nilai protected
        self._nilai = 85
        return self._nilai


# Membuat objek dari kelas Mahasiswa
bagus = Mahasiswa('Bagus', "2144432")
# Metode protected masih dapat diakses (meskipun sebaiknya tidak)
print(bagus._hitung_nilai_akhir())

# Private:
# Atribut atau metode yang bersifat private hanya bisa diakses dari
# dalam kelas itu sendiri. Tanda private diawali dengan dua underscore (`__`).
class Dosen:
    def __init__(self, nama):
        # Atribut private
        self.__gaji = 10000000
        # Atribut public
        self.nama = nama

    # Metode private
    def __tampilkan_gaji(self):
        return f"Gaji {self.nama} adalah {self.__gaji}"

    # Metode public untuk mengakses private
    def tampilkan_gaji(self):
        return self.__tampilkan_gaji()


# Membuat objek dari kelas Dosen
andi = Dosen('Andi')
# Tidak bisa mengakses atribut atau metode private secara langsung
# print(andi.__gaji)  # Akan error
# print(andi.__tampilkan_gaji())  # Akan error

# Hanya bisa diakses melalui metode public
print(andi.tampilkan_gaji())

# Kesimpulan:
# Public: Bebas diakses oleh siapa saja.
# Protected: Sebaiknya hanya diakses oleh kelas dan turunannya.
# Private: Hanya bisa diakses dari dalam kelas itu sendiri.
