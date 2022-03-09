def garis():
    print("------------------------------")

#fungsi bubble sort ascending (dari kecil ke besar)
def sort_asc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range (n):
        #perulangan kedua
        for j in range (n-i-1):
            #membandingkan masing" elemen ke kanan
            if array[j] > array[j+1]:
                #jika lebih besar, tukar ke kiri
                array[j], array[j+1] = array[j+1], array[j]
    return array

#fungsi bubble sort descending (dari besar ke keci)
def sort_dsc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range (n):
        #perulangan kedua
        for j in range (n-i-1):
            #membandingkan masing" elemen ke kanan
            if array[j] < array[j+1]:
                #jika lebih besar, tukar ke kiri
                array[j], array[j+1] = array[j+1], array[j]
    return array

#fungsi rata rata
def rata_rata(angka):
   return sum(angka) / len(angka)


#input nilai
garis()
nama =(input("Masukan Nama Anda : "))
nilai_1 =  int(input("Nilai 1 : "))
nilai_2 =  int(input("Nilai 2 : "))
nilai_3 =  int(input("Nilai 3 : "))
nilai_4 =  int(input("Nilai 4 : "))
nilai_5 =  int(input("Nilai 5 : "))
nilai_6 =  int(input("Nilai 6 : "))
nilai_7 =  int(input("Nilai 7 : "))
nilai_8 =  int(input("Nilai 8 : "))
nilai_9 =  int(input("Nilai 9 : "))
nilai_10 =  int(input("Nilai 10 : "))
angka = [nilai_1, nilai_2, nilai_3, nilai_4, nilai_5, nilai_6, nilai_7, nilai_8, nilai_9, nilai_10]
garis()
print()


#nilai akhir
print("HASIL AKHIR----")
#nama
print("Nama Anda : ",(nama))
print("Urutan Angka ascending : ",(sort_asc(angka)))
print("Urutan Angka dencending : ",(sort_dsc(angka)))

#cari angka terbesar
print("Angka Terbesar:", max(angka))

#cari angka terkecil
print("Angka Terkecil:", min(angka))

#jumlahkan angkanya
print("Jumlahkan Angka:", sum(angka))

#rata_rata
print("Rata-ratanya:", (rata_rata(angka)))
