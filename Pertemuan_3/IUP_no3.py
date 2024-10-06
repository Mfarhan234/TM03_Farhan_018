# input 0 =  tccccct
# output 0 = 396000 Dolar Imbu
# input 1 = onetrypastiACIniBukanCPIniBukanCTF
# output 1 = Di gudang tersisa 34 batu
#            Wah, Jotaro Joemama tidak jadi dipecat

s = input("Masukkan Batu yang akan anda simpan : ") # masukkan batu yang ingin anda simpan

if 1 <= len(s) <= 100000: #memberi batas input 
    batu_sisa = None # digunakan untuk menyimpan batu yang tidak saling menghjancurkan
    kerugian_kesuluruhan= 0 # Variabel ini digunakan untuk menyimpan jumlah kerugian dari batu yang saling menghancurkan
    for batu in s : 
        if batu_sisa and batu_sisa[-1] == batu : # mengecek apakah batu_sisa kosong atau terdapat elemen, dan batu adalah batu terakhir di batu_sisa
            jenis_batu = batu_sisa.pop() # menghapus (pop) batu terakhir dari sisa_batu karena saling menghancurkan, jenis-batu menyimpan nilai batu yg dihapus
            nilai_ascii = ord(jenis_batu) # total nilai ASCII dari batu yang hancur, ord()untuk mengembalikan kode ASCII karakter
            kerugian_batu = 1000 * nilai_ascii * 2 # kerugian dari 2 batu yang hancur dan dikali 1000
            kerugian_kesuluruhan += kerugian_batu # menambahkan kerugian dari batu yang hancur ke kerugian
        else:
            batu_sisa.append(batu) #Jika batu saat ini berbeda dengan batu terakhir di batu_sisa, batu saat ini ditambahkan ke batu_sisa
    batu_sisa_count = len(batu_sisa) # menghitung batu yang tersisa di batu_sisa setelah diproses semuanya
    print(f"Di gudang tersisa {batu_sisa_count} batu") # print total batu yang tidak hancur
    if kerugian_kesuluruhan > 0:
        print(f"Total kerugian : {kerugian_kesuluruhan} Dolar Imbu") #print kerugian 
    else:
        print("Wah, Jotaro Joemema tidak jadi dipecat")  #print nasib jotaro 
else :
    print ("Batu yang anda masukkan melebihi batas") # print jika input tidak sesuai 