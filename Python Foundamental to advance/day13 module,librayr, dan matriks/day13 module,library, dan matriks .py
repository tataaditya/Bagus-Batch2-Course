# disini kita akan mempelajari banyak hal yah wkwk
# kita akan mempelajari library, module, dan matriks :')
# perbedaan module dan library, library adalah high level dari module
# yuk kita mulai


# module dan library
# kita bisa dengan mudah mengakses mesin yang sudah disiapkan oleh komunitas python
# mirip seperti fungsi tapi yang sudah dibikin org lain, kita tinggal pake aja
# caranya dinamakan import

import math # untuk kalkulasi
import numpy as np # untuk kalkulasi matriks yang rumit

# kita pakai modul math dulu
hasil_akar = math.sqrt(16) #sqrt untuk mendapatkan akar
hasil_pangkat = math.pow(2,3) #pow untuk pangkat

# kita juga bisa mengakses fungsi khusus kalau mau
# guna efisiensi biar ngga berat
from math import sqrt
print(sqrt(25)) # Output: 5.0

# nah skrg kita juga bisa kasih alian
# misal pada import library
import numpy as np

# fungsinya biar ngga ribet ngetik numpy aja sih
array = np.array([1, 2, 3])
print(array)

# ini yang menarik, kita juga bisa bikin module buatan kita sendiri
import nyapa

nyapa.sapa("tata")

# matriks kita pindah file yah ribet soalnya
