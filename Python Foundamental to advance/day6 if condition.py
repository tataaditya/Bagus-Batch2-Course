# if condition
# digunkan untuk logika untuk mengambil jalan, diantara beberapa kasus

nilai = 75

# jika nilai diatas 70 maka lulus
# kalau selain itu maka tidak lulus
if nilai >70:
    print('Kamu lulus')
else:
    print('Kamu tidak lulus')
    
# Praktik membuat Program yang menyimpan nama nama cowo redflag danw warna baju cowo redflag
#Minta input pengguna warna baju mereka, nama mereka siapa. Cek kondisi..

nama = input(str("Nama Kamu siapa ?"))
baju = input(str("Bajunya warna apa ?"))

red_flag = ["bagus","yogi","abdan","andika","semua cowo kecuali tata"]
warna= ["merah","biru","skena"]

if nama in red_flag and  baju in warna:
  print("------------------")
  print("Kamu cowo red flag")

else:
  print("------------------")
  Tata = input(str("tunggu kamu tata bukan ??"))
  if Tata == "ya":
    print("kamu greenflag banget 🥰")
  else:
    print("kamu maroon flag deh")