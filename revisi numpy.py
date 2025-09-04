# list daftar belanja bulanan di kost
list_belanja=["Sabun", "Tisu", "Odol", "Sunscreen"]
print("List belanja awal:", list_belanja)

# tambah barang baru
list_belanja.append("Parfume")
print("Setelah tambah barang:", list_belanja)

# hapus barang (masih ada di kost)
list_belanja.remove("Odol")
print("Setelah hapus barang:", list_belanja)

# update nama barang (typo ki kodong)
list_belanja[1]="Tisu Wajah"
print("Ganti nama barang:", list_belanja)

# menampilkan list barang langsung
print("fix belanjaan:", list_belanja)

import array as arr
# membuat array bertipe ineteger (harga barang belanja bulanan)
# harga awal
harga=arr.array('i',[20000, 15000, 30000, 40000])

# operasi dasar
harga.append(75000)   #harga produk baru
harga.remove(30000)   #hapus harga yg tidak jadi beli
harga[1]=13500        #update harga (ada diskon)

# menampilkan harga
print("list harga:",end="")
for x in harga:
    print(x,end="")


# list 
list_dihapusdiganti=["Odol",30000,"Tisu",15000]
list_dihapusdiganti.append(True)
print("list dihapusdiganti:",list_dihapusdiganti)

# Array dengan modul array
harga_array=arr.array('i',[20000, 135000, 40000])
harga_array.append(75000)
print("Fix Harga(module array):",harga_array.tolist())


# Array dengan NumPy
import numpy as np
nilai_tugas=np.array([80, 85, 90, 95, 99])
print("Nilai tugas:", nilai_tugas)
print("Operasi aritmatika(+10):", nilai_tugas+10)

# pembuatan array numpy
nilai=np.array([88, 90, 95, 100])
print("Mau nilai:", nilai)


# MATRIKS dengan numpy
# membuat array berisi nol
zeros=np.zeros((3,9))  #array 3x9
print(zeros)

# membuat array berisi satu
ones=np.ones((3,3))
print(ones)

# membuat array dengan rentang nilai (seperti range())tapi lebih fleksibel
arr=np.arange(3,9,6)
print(arr)

# membuat array dengan jumlah elemen tertentu yg dibagi rata dlm suatu interval
linspace=np.linspace(0,10,5)
print(linspace)

# membuat array dengan nilai acak dari distribusi seragam (0 hingga 1)
random_arr=np.random.randint(0,10, size=(9,9))
print(random_arr)

# mengetahui bentuk dan dimensi array
a=np.array([[3,9],[0,6]]);a.shape; a.ndim
print(a)

# mengetahui atau mengatur tipe data
tes=np.array([1,2,3],dtype="float32").dtype
print(tes)

# menghitung total elemen
tes=np.array([[0,3],[0,9],[0,6]]).size
print(tes)

# akses dan manipulasi data
a=np.array([30,90,60,91]);a[1:3]
print(a)


