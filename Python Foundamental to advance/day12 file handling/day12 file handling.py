# disini kita akan mempelajari bagaimana caranya mengakases file
# ada banyak caranya beserta fungsinya tapi akan kita jabarkan beberapa yah
#  ingat pada setiap membuka file !! harus dan wajib ditutup yah
# file.close()

file = open(r"day12 file handling\file.txt","r")
isi = file.read()
print(isi)
# # !! Harus selalu ditutup yah.. karena alokasi file akan terus berjalan kalau ngga ditutup
# file.close()

# oke sekarang yang kita ingin ngambil atasnya atau baca semuanya
# kemarin aku coba ngga bisa akses satu file untuk beberapa kegiatan sekaligus
# jadinya kita bikin 2 variabel dlu aja yah
file1 = open(r"day12 file handling\file.txt",'r')
file2 = open(r"day12 file handling\file.txt",'r')

# isi1 = file.readline() # ngambil atasnya aja
isi2 = file2.readlines() # ngambil semua data cuman berbentuk list
print(isi2)

# fungsi write
# kalau mau nulis perhatikan 2 metode "w" dan "a"
# untuk menimpa
file = open(r"day12 file handling\file.txt",'w')
file.write("Kamu abis operasi yah ??")

# untuk menambahkan
file1 = open(r"day12 file handling\file.txt",'a')
file.write("\nciee tbtb aku nongol\n")
file.close()

# !! write otomatis buat file jika ngga ada filenya

# with cara praktis untuk membuka dan menutup file
with open(r"day12 file handling\file.txt",'w') as file:
  file.write("hai")

#  kita pake fungsi sekarang
# fungsi ini akan mencetak "hai" disetiap file yang kamu masukin
def tulis(file_name):
  with open(file_name,'w') as file:
    file.write("hai")

tulis(r'day12 file handling\file.txt')

# project kecil kecilan sekarang
# Latihan project tebak angka manual
# latihan project tebak angka manual

# print nama pemain dan berapa kali percobaan
# buat variabel angka
# buat variabel jumlah coba
# Selama belum bisa menebak, simpan di variabel

# Angka rahasia (ditentukan manual)
# angka_rahasia = 25  # Ganti dengan angka yang diinginkan

# # Membuka file untuk menyimpan data pemain
# file_path = "data_pemain.txt"

# # Variabel untuk mencatat jumlah percobaan
# jumlah_coba = 0
# tebakan = None

# # Meminta nama pemain
# nama_pemain = input("Masukkan nama Anda: ")

# # Proses menebak angka
# print("Tebak angka antara 1 sampai 100!")
# while tebakan != angka_rahasia:
#     try:
#         tebakan = int(input("Masukkan tebakan Anda: "))
#         jumlah_coba += 1

#         if tebakan < angka_rahasia:
#             print("Terlalu kecil!")
#         elif tebakan > angka_rahasia:
#             print("Terlalu besar!")
#         else:
#             print(f"Selamat, {nama_pemain}! Anda berhasil menebak angka dalam {jumlah_coba} percobaan.")
#     except ValueError:
#         print("Harap masukkan angka yang valid.")

# # Menyimpan data pemain ke file
# with open(file_path, "a") as file:
#     file.write(f"Nama: {nama_pemain}, Percobaan: {jumlah_coba}\n")

