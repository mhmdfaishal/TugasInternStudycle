# Dokumen Program
**Cara Penggunaan**
* Buka CMD pada direktori file program
* Ketik *python bilangan.py* lalu Enter
* Masukkan banyak bilangan
* Masukkan nilai bilangan
* Output akan keluar sesuai dengan program yang dibuat

**Cara Kerja Program**
* Bubble Sort
    * Fungsi akan menerima list bilangan
    * Nilai setiap masing-masing indeks pada list akan dibandingkan besarnya
    * Jika nilai[i] lebih besar dari nilai[i+1], maka nilai[i] akan disimpan kedalam variabel temp lalu nilai[i+1] akan disimpan kedalam nilai[i] dan nilai[i+1] akan diisi dengan nilai temp sehingga kedua nilai akan bertukar
    * Fungsi tersebut akan terus melakukan looping hingga semua bilangan terurut dari yang terbesar hingga ke terkecil
* Nilai rata-rata bilangan
    * Membuat sebuah variabel *sum* untuk menyimpan jumlah dari semua nilai yang terdapat pada list
    * Melakukan looping untuk menjumlahkan semua nilai yang terdapat pada list lalu menyimpannya pada variabel *sum*
    * Menghitung nilai rata-rata bilangan dengan rumus *average = sum/panjang list(banyak data)*
* Nilai tengah bilangan
    * Membuat sebuah kondisi jika banyak data bernilai genap atau ganjil
    * Jika banyak data bernilai genap maka masuk kedalam kondisi yang pertama yaitu:
        * Menghitung index 1 = banyak data//2
        * Menghitung index 2 = (banyak data//2) + 1
        * Menghitung median yaitu median = (nilai[index1-1]+nilai[index2-1])//2
    * Jika banyak data bernilai ganjil maka masuk kedalam kondisi kedua yaitu:
        * Menghitung index nilai = (banyak data//2)+1
        * Menghitung median yaitu nilai[index-1]
* Hasil perkalian bilangan
    * Membuat variabel *mul* dengan nilai 1
    * Melakukan looping untuk mengalikan semua nilai yang terdapat pada list lalu menyimpannya pada variabel *mul*

**Limitasi Program**
* Program tidak bisa menerima input berupa string atau karakter
* Program tidak bisa menerima input bilangan yang kurang dari sama dengan 0
* Program hanya bisa menerima input berupa bilangan bulat

