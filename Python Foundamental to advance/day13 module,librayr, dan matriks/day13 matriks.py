# yuk kita membuat matriks tanpa menggunakan python

# Membuat matriks 2x2
matriks = [[1, 2], [3, 4]]
print(matriks)
# Output:
# [[1, 2], [3, 4]]

# Penjumlahan Matriks Tanpa NumPy
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

hasil_penjumlahan = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print(hasil_penjumlahan)
# Output:
# [[6, 8], [10, 12]]

# Perkalian Matriks Tanpa NumPy
hasil_perkalian = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
print(hasil_perkalian)
# Output:
# [[19, 22], [43, 50]]

# wkwk gimana kalau tranpose ?? dll
# kalau dengan numpy jadi begini :
print("""
      \n\n
      DADAH RIBET KITA MENGGUNAKAN NUMPY SEKARANG
      
      """)

import numpy as np

# Membuat matriks 2x2
matriks = np.array([[1, 2], [3, 4]])
print(matriks)
# Output:
# [[1 2]
#  [3 4]]

# penjumlahan matriks 
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

hasil = A + B
print(hasil)
# Output:
# [[ 6  8]
#  [10 12]]

# perkalian matriks
A = np.array([[1, 2], [3, 4]])

hasil = A.T
print(hasil)
# Output:
# [[1 3]
#  [2 4]]

# invers matriks
A = np.array([[1, 2], [3, 4]])

hasil = np.linalg.inv(A)
print(hasil)
# Output:
# [[-2.   1. ]
#  [ 1.5 -0.5]]
