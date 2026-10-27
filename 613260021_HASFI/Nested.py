# ===================================================
# PRAKTIKUM 4: NESTED LOOP DAN PENGOLAHAN LIST 
# SIMPAN SEBAGAI: PRAKTIKUM_04.PY
# ===================================================

for baris in range(1, 4):
    for kolom in range(1, 4):
        print(f"{baris}x{kolom}={baris*kolom}", end=" ")
    print()   #pindah baris

# 2. pengenalan list data nilai 
nilai_maba = [12, 32-35]
nilai_maba.append(95)

print("daftar nilai :", nilai_maba)
print("nilai tertinggi:", max(nilai_maba))