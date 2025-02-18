import tkinter as tk

root = tk.Tk()
root.title("Kalkulator Penjummlahan")
root.geometry('400x300')


text_angka1 = tk.Label(root, text='Angka 1 :')
text_angka1.grid(column = 0, row = 0)
# disini kita ngga menggunakan .pack melainkan .place()
# text_angka1.place(x = 50, y = 10)

entry_angka1 = tk.Entry(root)

# bisa pake grid bisa pake place sesuaikan aja
entry_angka1.grid(column=1, row=0)

root.mainloop()