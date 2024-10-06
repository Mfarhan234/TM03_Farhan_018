# sample input 0
# 4 
# 3 1 2 1
# output = 2
# Sample input 1 
# 1
# 1 
# Output = 0 
N = int(input("Input jumlah ruangan anda : ")) # input jumlah ruangan yang diinginkan 
Warna_Tema = list (map(int, input("input ruangan yang telah dicat : ").split())) # input ruangan yang telah dicat berdasarkan tema 
# list berfungsi untuk mengubah hasil dari map menjadi list agar bisa di fungsi count
if 1 <= N <= 100000: # Batasan nilai N
    maks_N = max(Warna_Tema.count(i) for i in (Warna_Tema))  # maksimal ruangan yang dicat dengan warna yang sama, count untuk menghitung seberapa sering warna yang muncul dalam Warna_Tema
    ruangan_dicat_ulang = N - maks_N  # Jumlah ruangan yang perlu dicat ulang agar disetiap ruangan memiliki tema warna yang sama 
    print (ruangan_dicat_ulang) # Print hasil
else:
    print("Angka yang anda masukkan tidak sesuai")
