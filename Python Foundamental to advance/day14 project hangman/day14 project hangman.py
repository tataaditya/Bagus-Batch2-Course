import random
from bahan import *

# print judul dari modul bahan
print(title)

# print aturan permainan
print("""\
Aturan Permainan :
1. Selamatkan 'Budi' Dengan cara menjawab 1 pertanyaan dengan benar!
2. Budi hanya memiliki 6 nyawa!
3. 1 kesalahan akan mengurangi 1 nyawa Budi.
""")

siap = input("apakah kamu siap atau tidak ? (y/n)").lower

if siap == "y":
    # buka file peryanyaan
    file1 = open(r"day14 project hangman\pertanyaan.txt","r")
    # buka file jawaban
    file2 = open(r"day14 project hangman\jawaban.txt","r")
    
    # Baca deh
    pertanyaan = file1.readlines()
    jawaban = file2.readlines()
    
    # Variabel nyawa budi
    nyawa_budi = 6
    
    for i in range(6):
        # pilih pertanyaan secara acak 
        angka_random = random.randint(0, len(pertanyaan) - 1)
        pertanyaan_terpilih = pertanyaan[angka_random].strip()
        jawaban_benar = jawaban[angka_random].strip().lower()
        
        # Print hangman berdasarkan nyawa yang tersisa
        print(hangman[6 - nyawa_budi])
            
        # Print pertanyaan dan minta jawaban user
        print(f"Pertanyaan: {pertanyaan_terpilih}")
        jawaban_user = input("Jawaban kamu: ").strip().lower()

        # Cek jawaban
        if jawaban_user == jawaban_benar:
            print(congrats)
            print("Selamat! Kamu berhasil menyelamatkan Budi!")
            break
        else:
            nyawa_budi -= 1
            print(f"Salah! Nyawa Budi berkurang, sisa nyawa: {nyawa_budi}")

        # Jika nyawa habis
        if nyawa_budi == 0:
            print(hangman[0])
            print("Sayang sekali, Budi tidak dapat diselamatkan.")
            break

else:
    # Jika tidak siap
    print(hangman[6])
    print("Permainan berakhir.")