U = int(input())  # health point ucup
K = int(input())  # jumlah Knight iblis
M = int(input())  # Jumlah Minions Iblis

HP_minion, HP_Knight, HP_R_Iblis = 100, 500, 1000 # HP dari ketiga musuh
minion_aktif = M//2 # jumlah minion membeku
Knight_aktif = K//2 # jumlah
Damage_Ucup, D_Minion, D_Knight, D_R_iblis = 100, 2, 5, 100 # damage masing masing dari 4 tokoh 1

d_total_minions = minion_aktif * D_Minion * HP_minion / Damage_Ucup # damage total minions
d_total_knight = Knight_aktif * D_Knight * HP_Knight / Damage_Ucup # damage total knight
d_total_R_iblis = 1 * D_R_iblis * HP_R_Iblis / Damage_Ucup  # damage total raja iblis
damage_akhir = d_total_minions + d_total_knight + d_total_R_iblis # total damage yang diterima ucup dari ketiga musuh
new_u = U - damage_akhir  # total HP ucup setelah diserang
new_u = int (new_u)

if U < 1 or M < 1 or K < 1 :
    print ("Invalid Number")
elif U > 10**19 or M > 10**19 or K > 10*19:
    print ("Input terlalu over")
else:
    if new_u <= 0 :
        print ("Yah! Ucup Meninggoy.")
    if new_u > 0 :
        print (f"Yey! Ucup Menang! HP tersisa: {new_u}")