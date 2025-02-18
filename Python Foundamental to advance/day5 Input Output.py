# Melakukan Input
nama = str(input("Nama kamu siapa ? "))
print("Halo ",nama)

Hai = ['Nama','Bagus']
print(Hai)

# output
# Bisa pake koma (,)
print("hai",nama)

# Bisa pake plis (+), namun perlu penyamaan tipe data
print("Hai" + str(nama))

# Bisa pake format string (f'')
phi = 22/7
print(f"Nilai phi adalah {phi:.2f}") #fungsi dari {phi:.2f} biar ngga banyak angka dibelakang koma

# fungsi raw (r')
# fungsinya untuk melihat print seperti apa adanya tanpa diganggu \n dkk
print('\nhai namaku tata')
print(r'\nhai namaku tata')

# Program menghitung volume tabung menggunakan input
# Atribut yang kita perlukan
Jari_jari = int(input(("Jari jari dalam cm : ")))
Tinggi = int(input("Tinggi dalam cm : "))
phi = 22/7

# pengerjaan rumus
Volume_Tabung = phi * Jari_jari ** 2 * Tinggi
print(f"Volume tabung adalah {Volume_Tabung:.2f} cm")