# kali ini kita akan mempelajari bagaimana cara menggunakan function
# function intinya seperti kita membuat mesin untuk mencetak sesuatu...
# jadi kalau mesinya sudah terbuat kita tinggal panggil panggil aja deh

# membuat mesin untuk menyapa orang
def sapa_orang(nama):
    print(f"hai mas {nama}")
    
# kita memanggil mesin/ function
sapa_orang(input("siapa yang mau kamu sapa ??"))

#  membuat fungsi untuk hitung volume bola
def hitung_volume_bola(r):
    volume = (4/3) * 3.14 * r **3
    print(f"volume bola dengan jari jari {r} adalah {volume} cm^3")

# kita memanggil mesin/ function
hitung_volume_bola(int(input("masukan jari jari bola : ")))

print("\n++++++++")
# sekarang kita menggunakan fungsi return...
# gunanya setelah mesin mengolah nilai atau output,, maka outputnya akan tersimpan

def hitung_volume_bola(r):
    volume = (4/3) * 3.14 * r **3
    return volume

r = int(input("Masukan jari jari bola :"))
volume_bola = hitung_volume_bola(r)
print(volume_bola)


# Praktik ke 7 menggunakan function
# # menerapkan praktik minggu ke tujuh kedalam function
# def Tampilmenu():
#     print('\nPilih Bangun Datar : ')
#     print('1. Persegi ')
#     print('2. Persegi Panjang ')
#     print('3. Segitiga ')
#     print('4. Jajar Genjang ')
#     print('5. Lingkaran ')
#     print('6. Trapesium ')
#     print('7. Belah Ketupat ')
#     print('8. Layangan ')

# def Tampil():
#     print('\nPilih Bangun Ruang : ')
#     print('1. Kubus ')
#     print('2. Balok ')

# # Bangun datar
# def persegi():
#   sisi = float(input("Masukkan panjang sisi: "))
#   luas = sisi * sisi
#   print(f"Luas Persegi: {luas}")
#   return luas

# def persegi_panjang():
#   panjang = float(input("Masukkan panjang: "))
#   lebar = float(input("Masukkan lebar: "))
#   luas = panjang * lebar
#   print(f"Luas Persegi Panjang: {luas}")
#   return luas

# def segitiga():
#   alas = float(input("Masukkan alas: "))
#   tinggi = float(input("Masukkan tinggi: "))
#   luas = 0.5 * alas * tinggi
#   print(f"Luas Segitiga: {luas}")
#   return luas

# def jajar_genjang():
#   alas = float(input("Masukkan alas: "))
#   tinggi = float(input("Masukkan tinggi: "))
#   luas = alas * tinggi
#   print(f"Luas Jajar Genjang: {luas}")
#   return luas

# def lingkaran():
#   jari_jari = float(input("Masukkan jari-jari: "))
#   luas = 3.14 * jari_jari ** 2
#   print(f"Luas Lingkaran: {luas}")
#   return luas

# def trapesium():
#   sisi_atas = float(input("Masukkan sisi atas: "))
#   sisi_bawah = float(input("Masukkan sisi bawah: "))
#   tinggi = float(input("Masukkan tinggi: "))
#   luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
#   print(f"Luas Trapesium: {luas}")
#   return luas

# def layang_layang():
#   diagonal_1 = float(input("Masukkan diagonal 1: "))
#   diagonal_2 = float(input("Masukkan diagonal 2: "))
#   luas = 0.5 * diagonal_1 * diagonal_2
#   print(f"Luas Layang-Layang: {luas}")
#   return luas

# # Bangun Ruang
# def kubus():
#   sisi = float(input("Masukkan panjang sisi: "))
#   volume = sisi ** 3
#   print(f"Volume Kubus: {volume}")
#   return volume

# def balok():
#   panjang = float(input("Masukkan panjang: "))
#   lebar = float(input("Masukkan lebar: "))
#   tinggi = float(input("Masukkan tinggi: "))
#   volume = panjang * lebar * tinggi
#   print(f"Volume Balok: {volume}")
#   return volume

# print('Calculator Bangun Datar dan Bangun Ruang!')
# print('''Pilih Kategori :
# 1. Bangun Datar
# 2. Bangun Ruang ''')
# kategori = int(input('Pilihanmu : '))

# if(kategori == 1):
#     Tampilmenu()
#     pilihan_bDatar = int(input('Pilihanmu : '))

#     if pilihan_bDatar == 1:  # Persegi
#       persegi()

#     elif pilihan_bDatar == 2:  # Persegi Panjang
#       persegi_panjang()

#     elif pilihan_bDatar == 3:  # Segitiga
#       segitiga()

#     elif pilihan_bDatar == 4:  # Jajar Genjang
#       jajar_genjang()

#     elif pilihan_bDatar == 5:  # Lingkaran
#       lingkaran()

#     elif pilihan_bDatar == 6:  # Trapesium
#       trapesium()

#     elif pilihan_bDatar == 8:  # Layang-Layang
#       layang_layang()

#     else:
#         print("Pilihan tidak valid.")

# elif(kategori == 2):
#     Tampil()
#     pilihan_bRuang = int(input('Pilihanmu : '))

#     if pilihan_bRuang == 1:  # Kubus
#         kubus()

#     elif pilihan_bRuang == 2:  # Balok
#         balok()

#     else:
#         print("Pilihan tidak valid untuk bangun ruang.")

# else:
#     print("Pilihan kategori tidak valid.")