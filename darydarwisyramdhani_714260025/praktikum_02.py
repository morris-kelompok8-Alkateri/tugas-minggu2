angka = int(input("Masukkan angka: "))
is_prima = True  # Flag penanda

if angka < 2:
    is_prima = False
else:
    for pembagi in range(2, angka):
        if angka % pembagi == 0:
                is_prima = False  # Ditemukan pembagi selain 1 dan dirinya
                break             # Hentikan pencarian

    if is_prima:
        print(f"{angka} adalah BILANGAN PRIMA")
    else:
        print(f"{angka} BUKAN bilangan prima")