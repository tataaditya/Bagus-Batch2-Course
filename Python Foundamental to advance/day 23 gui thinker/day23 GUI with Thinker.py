# kita akan mempelajari GUI biar ramah user

# import library, kalau belum ada bisa pip intall tk di terminal
import tkinter as tk

root = tk.Tk() #display , ini sebuah objek yah
root.title("Basic Kalkulator") #method 
root.geometry("400x300") #method untuk lebar kali tinggi


# fungsi untuk diisi command dibawah
def on_click():
    label2.config(text=f'Halo {entry.get()}')

# kita akan membuat label
# Label banyak banget parameternya, kita pakai beberapa
# Parameter :
# 1. root yah
# 2. Kita bisa masukan text
label = tk.Label(root, text="Masukan Nama : ")

# .pack() untuk automatisasi letak
label.pack(pady = 10)

# entry
entry = tk.Entry(root)
entry.pack(pady = 10)

# Kita akan membuat button
button = tk.Button(root, text='kirim', command = on_click)
button.pack(pady=10)

# untuk dimasukan ke function
label2 = tk.Label(root, text='')
label2.pack(pady=10)

# digunakan untuk mengeluarkan GUI bedasarkan looping
root.mainloop()

