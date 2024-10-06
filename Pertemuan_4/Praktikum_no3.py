cx, cy = map(int, input().split()) # Input Titik pusat lingkaran
T_awal_x, T_awal_y =  map(int, input().split()) # Input Titik awal King
T_akhir_x, T_akhir_y =  map(int, input().split()) # Input Titik Akhir King

jarak = ((T_akhir_x - T_awal_x)**2 + (T_akhir_y - T_awal_y)**2) #Menghitung jarak King

j_akhir_ke_pusatlingkaran = ((T_akhir_x - cx)**2 + (T_akhir_y - cy)**2) # Jarak titik akhir King ke pusat lingkaran

Time_to_end = jarak #jarak adalah waktu yang dibutuhkan King sampai ke titik akhir 

if j_akhir_ke_pusatlingkaran > Time_to_end :
    print("Yes") # Melakukan cek apakah raja sampai lebih cepat sampai ke titik akhir 
else:
    print("No") # jika jarak atau waktu raja ke titik akhir lebih besar atau lambat daripada jarak titik pusat ke T_akhir maka print No