# disini kita mulai masuk tipe data list dkk
# intinya tipe data list itu kumpulan dari data data yang ada di day 1
# kayak int atau str

# list
my_list = [1,'dua', 3.0]
print(my_list)

# kita masukin indeks [] untuk akses nilai tertentu
# Sesuai yang diinginkan, indeks dimulai dari 0 yah
print(my_list[-1])

# atau bisa juga begini
print('\n')
Teman = ['Bagus','Agung','andhinne',"admin bagus"]
sahabat = (Teman[0])
bukan_sahabat = (Teman[3])

print("sahabatku orang dibawah :"),print(sahabat)
print("bukan adalah orang dibawah :"),print(bukan_sahabat)


# kita juga bisa modifikasi sebuah list seperti :
# Modufikasi Sebuah list
print('\nDibawah adalah hasil modifikasi kami')
Teman[3] = 'udah ngga temen lagi'
print(Teman)

print('\nMenambahkan Data baru')
# untuk menambahkan elemen dibelakanh list
Teman.append('ada teman baru nih dibelakang')
# kalau nambah teman di tengah
Teman.insert(1,'Temen baru ditengah')
print(Teman)

# untuk menghapus gunakan remove
Teman = ['Bagus','Agung','andhinne',"admin bagus"]
Teman.remove("Agung")
print(Teman)

# .pop() menghilangkan data paling belakang
Teman.pop()
print(Teman)

# .Sort, untuk mengurutkan
Teman = ['Bagus','Agung','andhinne',"admin bagus"]
Teman.sort()
print(Teman)