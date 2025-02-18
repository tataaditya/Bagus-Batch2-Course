# kita akan membahas mengenai inheritince dan polimorism 
# Superclass (kelas induk) -> Pengguna
# Kelas ini merepresentasikan pengguna umum
class Pengguna:
    def __init__(self, nama, id_anggota):
        # Atribut public, bisa diakses di mana saja
        self.nama = nama
        self.id_anggota = id_anggota

    def info(self):
        # Metode untuk menampilkan informasi pengguna
        print(f"Nama: {self.nama}\nID Anggota: {self.id_anggota}")

    def hak_akses(self):
        # Metode untuk menampilkan hak akses pengguna umum
        print("Pengguna umum hanya bisa melihat data.")

# Subclass (kelas anak) -> Admin
# Kelas ini adalah turunan dari Pengguna, dengan tambahan fitur khusus untuk admin
class Admin(Pengguna):
    def __init__(self, nama, id_anggota, jabatan):
        super().__init__(nama, id_anggota)  # Memanggil constructor dari superclass
        self.jabatan = jabatan  # Atribut tambahan untuk admin

    def remove_account(self, nama_akun):
        # Metode untuk menghapus akun pengguna
        print(f"Akun dengan nama {nama_akun} telah dihapus.")

    def info(self):
        # Metode untuk menampilkan informasi admin (overriding metode dari superclass)
        super().info()
        print(f"Jabatan: {self.jabatan}")

    def hak_akses(self):
        # Metode untuk menampilkan hak akses admin (overriding)
        print("Admin memiliki akses penuh.")

# Membuat objek dari kelas Admin dan Pengguna
adm1 = Admin("Tata", "ADM001", "Manajer")
peng1 = Pengguna("Bagus", "2234567")

# Menampilkan hak akses masing-masing
peng1.hak_akses()  # Output: Pengguna umum hanya bisa melihat data.
adm1.hak_akses()  # Output: Admin memiliki akses penuh.

# ==========================================================

# Superclass -> Kalkulator Sederhana
# Kelas ini berisi operasi dasar seperti tambah, kurang, kali, dan bagi
class Kalkulator:
    def __init__(self, angka1, angka2):
        # Atribut untuk menyimpan dua angka yang akan dihitung
        self.angka1 = angka1
        self.angka2 = angka2

    def tambah(self):
        # Metode untuk penjumlahan
        return self.angka1 + self.angka2

    def kurang(self):
        # Metode untuk pengurangan
        return self.angka1 - self.angka2

    def kali(self):
        # Metode untuk perkalian
        return self.angka1 * self.angka2

    def bagi(self):
        # Metode untuk pembagian
        return self.angka1 / self.angka2

# Subclass -> Kalkulator Ilmiah
# Kelas ini menambahkan fitur operasi trigonometri dan pangkat ke Kalkulator
import math  # Library matematika Python

class KalkulatorIlmiah(Kalkulator):
    def __init__(self, angka1, angka2):
        # Memanggil constructor dari superclass
        super().__init__(angka1, angka2)

    def penjumlahan_sin(self):
        # Menjumlahkan sinus dari dua angka (dalam derajat)
        sin1 = math.sin(math.radians(self.angka1))
        sin2 = math.sin(math.radians(self.angka2))
        return sin1 + sin2

    def penjumlahan_cos(self):
        # Menjumlahkan cosinus dari dua angka (dalam derajat)
        cos1 = math.cos(math.radians(self.angka1))
        cos2 = math.cos(math.radians(self.angka2))
        return cos1 + cos2

    def penjumlahan_tan(self):
        # Menjumlahkan tangen dari dua angka (dalam derajat)
        tan1 = math.tan(math.radians(self.angka1))
        tan2 = math.tan(math.radians(self.angka2))
        return tan1 + tan2

    def penjumlahan_pangkat(self):
        # Menjumlahkan hasil pemangkatan angka1^2 + angka2^2
        return math.pow(self.angka1, 2) + math.pow(self.angka2, 2)

# Membuat objek dari KalkulatorIlmiah
sci_calc = KalkulatorIlmiah(30, 45)

# Menggunakan metode KalkulatorIlmiah
print("Hasil sin(30) + sin(45):", sci_calc.penjumlahan_sin())
print("Hasil cos(30) + cos(45):", sci_calc.penjumlahan_cos())
print("Hasil tan(30) + tan(45):", sci_calc.penjumlahan_tan())
print("Hasil 30^2 + 45^2:", sci_calc.penjumlahan_pangkat())
