# membuat kalkulator berbagai bangun
# DataBase kita
kategori_kalkulator = ["Bangun Datar", "Bangun Ruang"]
bangun_datar = ["persegi", "persegi panjang", "segitiga", "jajar genjang", "lingkaran", "trapesium", "belah ketupat", "layang-layang"]
bangun_ruang = ["balok", "kubus"]

# Input awal
print("Selamat datang di kalkulator milik tata")
print("""
   ________
  /////////|
 ///////// |
|||||||||  |
|||||||||  |
||||||||| /
|||||||||/
""")

print("Kalkulator ini akan menghitung Bangun Datar dan Bangun Ruang")
print("1. Ya, tampilkan list kategori")
print("2. Tidak, langsung lanjut")
input_user = int(input("Apakah kamu mau melihat daftar kategori? (1/2): "))

# ngeliatin database kita
if input_user == 1:
    print("\nKategori Bangun Datar:")
    for bangun in bangun_datar:
        print(f"- {bangun}")
    print("\nKategori Bangun Ruang:")
    for bangun in bangun_ruang:
        print(f"- {bangun}")
# kalau sselain 2 bakal error
elif input_user != 2:
    print("Pilihan tidak valid. keluar kamu kakanda")
    
# memilih kategori kalkulator
print("\n1. Bangun Datar")
print("2. Bangun Ruang")

kategori = input("Apa yang ingin kamu hitung? (1/2): ")
if kategori == "1":
    print("\nPilih bangun datar yang ingin dihitung:")
    
    # enumerate digunakan untuk otak atik indeks
    # for disini looping yah, ngga usah dihiraukan dlu
    # fokus ke if elsenya saja sama variabel
    # looping akan kita bahas di day berikutnya
    
    
    for i, bangun in enumerate(bangun_datar, 1):
        print(f"{i}. {bangun}")
    pilihan = int(input("Masukkan nomor bangun datar: "))
    
    # Jadi skrg indeksnya sesuai 1-8
    if 1 <= pilihan <= len(bangun_datar):
        bangun_terpilih = bangun_datar[pilihan - 1]
        if bangun_terpilih == "persegi":
            sisi = float(input("Masukkan panjang sisi: "))
            luas = sisi ** 2
            print(f"Luas persegi adalah {luas}")
        elif bangun_terpilih == "persegi panjang":
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            luas = panjang * lebar
            print(f"Luas persegi panjang adalah {luas}")
        elif bangun_terpilih == "segitiga":
            alas = float(input("Masukkan panjang alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            luas = 0.5 * alas * tinggi
            print(f"Luas segitiga adalah {luas}")
        elif bangun_terpilih == "jajar genjang":
            alas = float(input("Masukkan panjang alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            luas = alas * tinggi
            print(f"Luas jajar genjang adalah {luas}")
        elif bangun_terpilih == "lingkaran":
            phi = 3.14159
            r = float(input("Masukkan jari-jari: "))
            luas = phi * r ** 2
            print(f"Luas lingkaran adalah {luas}")
        elif bangun_terpilih == "trapesium":
            sisi1 = float(input("Masukkan sisi 1: "))
            sisi2 = float(input("Masukkan sisi 2: "))
            tinggi = float(input("Masukkan tinggi: "))
            luas = 0.5 * (sisi1 + sisi2) * tinggi
            print(f"Luas trapesium adalah {luas}")
        elif bangun_terpilih == "belah ketupat":
            diagonal1 = float(input("Masukkan diagonal 1: "))
            diagonal2 = float(input("Masukkan diagonal 2: "))
            luas = 0.5 * diagonal1 * diagonal2
            print(f"Luas belah ketupat adalah {luas}")
        elif bangun_terpilih == "layang-layang":
            diagonal1 = float(input("Masukkan diagonal 1: "))
            diagonal2 = float(input("Masukkan diagonal 2: "))
            luas = 0.5 * diagonal1 * diagonal2
            print(f"Luas layang-layang adalah {luas}")
    else:
        print("Pilihan tidak valid. Pulang aja sana.")
elif kategori == "2":
    print("\nPilih bangun ruang yang ingin dihitung:")
    for i, bangun in enumerate(bangun_ruang, 1):
        print(f"{i}. {bangun}")
    pilihan = int(input("Masukkan nomor bangun ruang: "))
    if 1 <= pilihan <= len(bangun_ruang):
        bangun_terpilih = bangun_ruang[pilihan - 1]
        if bangun_terpilih == "balok":
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            tinggi = float(input("Masukkan tinggi: "))
            volume = panjang * lebar * tinggi
            print(f"Volume balok adalah {volume}")
        elif bangun_terpilih == "kubus":
            sisi = float(input("Masukkan panjang sisi: "))
            volume = sisi ** 3
            print(f"Volume kubus adalah {volume}")
    else:
        print("Pilihan tidak valid.")
else:
    print("Pilihan tidak valid. Pulang aja njir.")