# contoh input 
# 1 
# 6 6
# output 
# Test Case #1: 
# 13
 
prima = [] # untuk menyimpan bilangan prima nanti
n  = 2 # untuk cek dari bilangan 2 yaitu bilangan prima pertama

for _ in range(1000000): # batasan bilangan prima yang akan diproses 
    b_prima = True # b_prima_awal dianggap bilangan prima dan benar
    for i in range (2, int(n**0.5)+ 1): # memeriksa bilangan dari 2 hingga akar kuadrat n untuk mencari faktor pembagi
        if n % i == 0 : # menentukan n bilangan prima atau bukan
            b_prima = False 
            break
    if b_prima :
        prima.append(n) # jika b_prima tetap True seteleah pemeriksaan, maka n adalah bilangan prima dan ditambahkan ke daftar prima
    n += 1 #menambah nilai n untuk memeriksa bilangan berikutnya

output = []
T = int(input()) # input nilai yang ingin dimasukan
if 1 <= T <= 40 : # batas nilai input
    for t in range (1, T + 1 ): # mengulangi setiap case dari 1 hingga T
        A, B = map (int, input().split()) # membaca 2 angka dari input pengguna 
        output.append(f"Test Case #{t} : ") #print hasil
        for p in prima[A-1:B]: #Mengambil bilangan prima dari daftar prima berdasarkan rentang A hingga B. A-1 digunakan karena daftar Python dimulai dari indeks 0.
            output.append(p) #mencetak setiap bilangan prima yang ditemukan
else:
    print("Invalid Number")

for o in output :
    print(o)