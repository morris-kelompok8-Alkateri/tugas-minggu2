# ===================================================
# PRAKTIKUM 3: DERET ARITMATIKA DAN AKUMULATOR
# Simpan sebagai: praktikum_03.py
# ===================================================

print("=== program hitung deret aritmatika ===")

awal = int(input("Masukan suku pertama (a): "))
beda = int(input("Masukan beda (b): "))

# 1. implementasi while: validasi input jumlah suku agar harus positif (> 0)
banyak =   int(input("Masukan jumlah suku (n): "))
while banyak <= 0:
    print("peringatan: banyak suku harus lebih dari 0!")
    banyak = int(input("silahkan masukan ulang banyak suku (n): "))

# 2. implementasi for & akumulator: mencetak dan menjumlahkan totalnya
suku = awal
total = 0 #celengan akumulator 

print("barisan deret: ", end="")
for i in range(banyak):
        print(suku, end=" ")
        total += suku
        suku += beda

print(f"total jumlah seluruh deret = {total}")


