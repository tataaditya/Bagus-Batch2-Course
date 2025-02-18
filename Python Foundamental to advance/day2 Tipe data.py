# Hai disini kita mulai day 2
# day 2 cukup mudah sebetulnya. Kita hanya akan mempelajari
# bagaimana Tipe-tipe data... 

# tipe data integer
# tipe data ini adalah tipe data yang bisa kita itung itung (kalkulasiin)

# misal ada angka 1
satu = 1 #tipe data integer
print(satu + satu)

# tipe data float
# sama sama bisa dikalkulasiin, cuman yang ini ada koma aja
satu = 1.0
print(satu + satu)

# kita hitung luas lingkaran
# rumusnya adalah pi*r kuadrat
pi = 22/7

# untuk ruas
r = 2

# rumus deh
luas = pi * r **2

# Kita tampilin hasil
print(luas)


# kita bikin yang lebih advance yuk
# kalkulasi harga diskon
print("\n \n")
print('+++++++++++++++++')
print('KALKULATOR DISKON')
harga_asli = 50000
nilai_diskon = 12 / 100
diskon = harga_asli*nilai_diskon
harga_setelah_diskon = harga_asli - nilai_diskon
print(harga_setelah_diskon)

# karena masih float, kita bisa mengubahnya dengan cara seperti ini agar jadi ineteger
print(int(harga_setelah_diskon))

