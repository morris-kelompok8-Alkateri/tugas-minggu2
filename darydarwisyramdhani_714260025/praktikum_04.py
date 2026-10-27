for baris in range(1, 4):
    for kolom in range(1, 4):
        print(f"{baris}x{kolom}={baris*kolom}", end=" ")
    print()  # Pindah baris

nilai_maba = [12, 32, 35]
nilai_maba.append(95)  

print("Daftar Nilai :", nilai_maba)
print("Nilai Tertinggi:", max(nilai_maba))