# kita akan mempelajari Perulangan
# ada 2 cara menggunakan perulangan
# 1 memakai for loop 
# fokus pada step yang kita mau


# 2 memakai while loop
# fokus pada finish

# ada fungsi range (jangkauan) (start,stop,step) / kalau satu doang (stop)
angka = [1,2,3,4,5,6]
for i in range (4):
    print(angka [i],end = '') #end digunakan agar ngga membuat enter di output

# ada fungsi len juga, biasanya untuk mengukur panjang suatu list dkk
print('\n++++++')
print(len(angka))
# coba kita gabungin sama perulangan
for i in range(len(angka)):
    print(angka[i])
    


# Mengerjakan kalkulasi Fibonacci
n = 5
hasil = 1

# start, stop, step
for i in range (n, 0 ,-1):
    hasil = hasil * i
    print(f'nilai i sekarang {i}')
    print(f'Nilai hasil sekarang {hasil}')
    
    
# Kalkulator faktorial
print("\n\nSelamat datang di kalkulator faktorial")
# Meminta input dari pengguna dan mengubahnya menjadi integer
input = int(input("pilih angka yang ingin kamu kalkulasikan : "))
# Variabel untuk menyimpan hasil faktorial
faktorial = 1
# Menghitung faktorial menggunakan loop
for i in range(input,0,-1):
    print('Nilai i sekarang adalah',i)
    print('dan nilai faktorial adalah',faktorial)
    faktorial = faktorial * i
# Menampilkan hasil faktorial
print('Nilai faktorial :', faktorial)

# while loop
# Akan selalu mengeksekusi sampai nilai False
print('\n\n')
n = -5
while n < 0:
    print(n)
    n = n+1

print(n)

    