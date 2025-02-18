import turtle
pen = turtle.Turtle()  # Membuat objek 'pen' dari modul turtle untuk menggambar
pen.speed(3)  # Mengatur kecepatan menggambar menjadi kecepatan 3 (sedang)

# Membuat sebuah kotak (kode di bawah ini dinonaktifkan dengan tanda komentar)
# for i in range(3):  
#     pen.forward(50)  # Maju sejauh 50 satuan
#     pen.left(120)  # Belok kiri sebesar 120 derajat

# Menggerakkan pen ke depan tanpa menggambar
pen.forward(100)  # Pen maju 100 satuan
pen.penup()  # Mengangkat pen supaya tidak menggambar saat berpindah
pen.goto(0, 100)  # Memindahkan posisi pen ke koordinat (0, 100)

# Menurunkan pen untuk mulai menggambar lagi
pen.pendown()  # Menurunkan pen untuk mulai menggambar
pen.forward(100)  # Pen menggambar garis lurus sepanjang 100 satuan

turtle.done()  # Menutup jendela setelah selesai menggambar


# Kode tambahan untuk menggambar rumah
import turtle
pen = turtle.Turtle()  # Membuat objek 'pen' lagi
pen.speed(0)  # Mengatur kecepatan menggambar menjadi tercepat

# Membuat kotak (kode di bawah ini juga dinonaktifkan)
# for i in range(3):  
#     pen.forward(50)
#     pen.left(120)

# Menggambar rumah

# Menggambar bagian bawah rumah (kotak)
pen.forward(30)  # Garis dasar sepanjang 30 satuan
pen.left(90)  # Belok kiri 90 derajat
pen.forward(40)  # Garis vertikal sepanjang 40 satuan
pen.left(90)  # Belok kiri 90 derajat
pen.forward(30)  # Garis atas sepanjang 30 satuan
pen.left(90)  # Belok kiri 90 derajat
pen.forward(40)  # Garis vertikal kembali ke dasar
pen.left(90)  # Kembali ke posisi awal

pen.penup()  # Mengangkat pen untuk berpindah posisi
pen.left(90)  # Mengubah arah pen
pen.forward(40)  # Pindah ke atas kotak untuk menggambar atap

# Menggambar atap rumah (segitiga)
pen.pendown()  # Menurunkan pen untuk menggambar
pen.right(30)  # Belok kanan 30 derajat
pen.forward(40)  # Garis pertama segitiga (atap)
pen.right(135)  # Belok kanan 135 derajat
pen.forward(40)  # Garis kedua segitiga (atap)

pen.penup()  # Mengangkat pen untuk berpindah posisi
pen.forward(-40)  # Kembali ke dasar atap
pen.right(-100)  # Mengatur ulang arah
pen.pendown()  # Menurunkan pen untuk menggambar lagi
pen.forward(100)  # Garis panjang ke belakang rumah
pen.right(100)  # Mengatur arah untuk melanjutkan gambar

# Menggambar belakang rumah
pen.forward(40)  # Garis horizontal belakang
pen.right(82)  # Belok kanan 82 derajat
pen.forward(100)  # Garis panjang vertikal belakang rumah
pen.penup()  # Mengangkat pen untuk berpindah posisi
pen.forward(-100)  # Kembali ke posisi awal

# Menggambar tembok belakang rumah
pen.pendown()  # Menurunkan pen untuk menggambar
pen.left(65)  # Belok kiri 65 derajat
pen.forward(40)  # Garis tembok vertikal
pen.right(65)  # Belok kanan 65 derajat
pen.forward(100)  # Garis tembok horizontal

# Menggambar pintu kecil di rumah
pen.penup()  # Mengangkat pen untuk pindah posisi
pen.right(24)  # Mengatur arah ke kanan 24 derajat
pen.forward(7.5)  # Pindah ke posisi pintu
pen.right(90)  # Belok kanan 90 derajat
pen.pendown()  # Menurunkan pen untuk menggambar pintu

pen.forward(20)  # Garis vertikal pintu
pen.left(90)  # Belok kiri 90 derajat
pen.forward(10)  # Garis horizontal atas pintu
pen.left(90)  # Belok kiri 90 derajat
pen.forward(20)  # Garis vertikal pintu kembali ke dasar

# Menghapus kepala pen untuk menyelesaikan gambar
pen.hideturtle()  # Menyembunyikan kursor pen
turtle.done()  # Menutup jendela setelah selesai menggambar