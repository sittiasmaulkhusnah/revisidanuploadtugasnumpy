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

# akses dan manipulasi data (Indexing&Slicing)
a=np.array([30,90,60,91]);a[1:3]
print(a)

# Statistical Functions
#1. numpy.amin() and numpy.amax()
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5])
min_value = np.amin(arr)
print("Nilai Minimum:", min_value)

max_value = np.amax(arr)
print("Nilai Maksimum:", max_value)

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5])
max_value = np.amax(arr)
print("Nilai Maksimum:", max_value)

#2. menghitung rentang (range) dari array (numpy.ptp())
range_value = np.ptp(arr)
print("\nArray:", arr)
print("Rentang:", range_value)

#3. numpy.percentile()
# membuat array NumPy 
arr = np.array([4, 8, 3, 9, 6, 2, 1, 5, 9])

# menghitung persentil ke-25 (Q1)
q1 = np.percentile(arr, 25)

# menghitung persentil ke-50 (median)
median = np.percentile(arr, 50)

# menghitung persentil ke-75 (Q3)
q3 = np.percentile(arr, 75)

# menampilkan hasil
print("Q1 (Persentil ke-25):", q1)
print("Median (Persentil ke-50):", median)
print("Q3 (Persentil ke-75):", q3)

#4. numpy.median()
# membuat array numpy
arr = np.array([4, 8, 3, 9, 6, 2, 1, 5, 9])

# menggunakan numpy.median() untuk menghitung median
median_value = np.median(arr)
print("Array:", arr)
print("Median:", median_value)

#5. numpy.mean()
arr = np.array([4, 8, 3, 9, 6, 2, 1, 5, 9])
mean = np.mean(arr)
print("Mean:", mean)

#6. numpy.average()
average = np.average(arr)
average = np.average(arr)
print("Average:", average)

#7. standard deviation
arr = np.array([4, 8, 3, 9, 6, 2, 1, 5, 9])

# menghitung standar deviasi dari array arr
std_deviation = np.std(arr)

print("Standar Deviasi:", std_deviation)

#7.1. Data berkelompok
interval = np.array([20, 30, 40, 50, 60, 70])  # Batas interval
frekuensi = np.array([5, 12, 18, 10, 7])       # Frekuensi

# menghitung midpoint dari setiap interval
midpoints = (interval[:-1] + interval[1:]) / 2

# menghitung mean dari data berkelompok
mean = np.sum(midpoints * frekuensi) / np.sum(frekuensi)

# menghitung variansi dari data berkelompok
varians = np.sum(((midpoints - mean) ** 2) * frekuensi) / np.sum(frekuensi)

# menghitung standar deviasi dari data berkelompok
std_deviation = np.sqrt(varians)

print("Mean:", mean)
print("Varians:", varians)
print("Standard Deviation:", std_deviation)

#8. variance
# Membuat array NumPy
arr = np.array([4, 8, 3, 9, 6, 2, 1, 5, 9])

# Menghitung varians dari array arr
variance = np.var(arr)

print("Array:", arr)
print("Varians:", variance)
