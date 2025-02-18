# kita akan mempelajari ERROR HANDLING
# error handling mencegah code yang rawan untuk error agar tidak terhenti
# jadi biar flow code terus berjalan walau ada yang error
# prinsipnya mirip if else atau If condition

# ada banyak jenis error handling
#  1. zero division error untuk ngga boleh 0
#  2. value error kalau valuenya tidak seharusnya seperti yang ditetapkan

# ok skrg kita praktik
# error (try and except)

try:
    num = int(input('Masukan nilai:'))
    hasil = 10/num
    print(num)
    
except ZeroDivisionError:
    print("Tidak boleh dibagi nol yah")
    
except ValueError:
    print(' Harus angka yah')
    
# kekuranganya disini harus mendefinisikan error satu persatu

# Nah skrg kalau mau menghindari semua kemungkinan error kita bisa menggunakan ini nih :
try:
    num = int(input('Masukan nilai:'))
    hasil = 10/num
    print(num)
except Exception as e:
    print(e)
