def FPB(A, B): # mencari FPB dari A dan B
    if B == 0: # jika b = 0 fungsi akan mengembalikan A dan menghentikan rekursi
        return A 
    return FPB(B, A % B) # mencari nilai pembagi diantara A dan B yang menghasilkan 0

def KPK(A, B) :   # mencari nilai KPK setelah mendapatkan FPB
    return A*B // FPB(A, B)     # Rumus mencari KPK 

A, B = map(int,input().split())     # meminta input pengiguna

C = FPB(A, B)    # C adalah FPB karena A dan B habis d bagi c , sesuai pernyataan soal
D = KPK(A, B)    # D adalah KPK karena nilai bilangan A atau B dikalikan suatu menghasilkan nilai D, sesuai pernyataan soal
Hasil_akhir = (C*D//A) + (C*D//B)     # Rumus menemukan bilangan A dan b sesuai petunjuk soal
print (Hasil_akhir)         # mencetak hasil akhir 
