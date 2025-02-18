# Tuple & Dictionary
# Membuat List = []
my_list = [1,"halo",3]
print(my_list)

# Membuat tuple = ()
# Tuple adalah immutable dimana tidak bisa diubah nilainya setelah ditetapkan
my_tuple = (1,"halo",3)
print(my_tuple)

# Dictionary
# Dimana tiap value memiliki key masing masing
my_kamus = {'umur':19,'nama':['Bagus',"19"]}
print(my_kamus["umur"])

# get, agar saat ngambil kalau tidak ada, ngga error
print(my_kamus.get("nama"))

# update
my_kamus.update({"age":20})
print(my_kamus)

# Menghapus
del my_kamus["age"]
print(my_kamus)

# clear
my_kamus.clear()
print(my_kamus)

data_mahasiswa = {
    '001':{'nama':'Abdan','umur':20},
    "120":{'nama':'Tata','umur':19}
}
print(data_mahasiswa['001']["umur"])

# Latihan
data_mahasiswa = {"ID" : {"nama":"Himmel","umur":23,"Nama orang tua":{"nama ayah":"Bambang","nama ibu":"Frieren"}},}
print(data_mahasiswa["ID"]["Nama orang tua"]["nama ayah"])
print(data_mahasiswa.get("ID", {}).get("Nama orang tua", {}).get("nama ayah", "Tidak ditemukan"))