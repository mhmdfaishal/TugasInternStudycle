'''''''''''''''''''''''''''''''''''''''''
Nama        : Muhammad Faishal Dienul Haq
Tanggal     : 29 Juni 2021
Deskripsi   : Program memasukkan bilangan lalu mengurutkannya dari terkecil hingga terbesar,
              serta menampilkan nilai rata-rata, nilai tengah, dan hasil perkalian dari semua bilangan
'''''''''''''''''''''''''''''''''''''''''
#fungsi bubble sort untuk mengurutkan nilai
def BubbleSort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j] > num[j+1]: 
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
                
num = []
sum = 0
print("=-=-=-=-=-=- Program Bilangan -=-=-=-=-=-=")
n = int(input('Masukkan banyak bilangan : '))
print("==========================================")
for i in range(0,n):
    x = int(input('Masukkan bilangan ke - '+ str(i+1) + ': '))
    num.append(x)   #memasukkan bilangan kedalam list
print("==========================================")
BubbleSort(num) #memanggil fungsi bubble sort untuk mengurutkan bilangan
print("\nUrutan bilangan (dari terkecil ke terbesar) =", num)

for j in range(0,n):
    sum = sum + num[j] #melakukan looping dengan menambahkan semua nilai yang ada pada list
    
average = sum/len(num)  #menginisasi nilai rata-rata = jumlah/banyak data
print("\nNilai Rata-rata dari bilangan =", average)

if(len(num) % 2 == 0):
    idx1 = len(num)//2  #menghitung index pertama
    idx2 = (len(num)//2) + 1    #menghitung index kedua
    median = (num[idx1-1]+num[idx2-1])//2 #menginisiasi nilai median = (nilai index pertama + nilai index kedua) / 2
else:
    idx = (len(num)//2)+1  #menghitung index
    median = num[idx-1]    #menginisiasi nilai median = nilai ke-index tersebut
        
print("Nilai tengah dari bilangan =", median)

mul = 1 #inisiasi variabel mul
for k in range(0,int(n)):
    mul = mul * num[k]  #melakukan looping dengan mengalikan setiap bilangan pada list

print("Hasil perkalian semua bilangan =", mul)
print("\n==========================================")
            