# ======================================================================
# TUGAS MANDIRI 1: KALKULATOR KONSOL BERMENU & MODUL OPERASI
# ======================================================================

import operasi3

while True:
    print("\n" + "=" * 45)
    print("KALKULATOR KONSOL BERMENU")
    print("=" * 45)
    print("1. Operasi Aritmatika Dasar (+, -, *, /)")
    print("2. Cek Sifat Bilangan Ganjil/Genap")
    print("3. Hitung Deret Aritmatika (For & Akumulator)")
    print("4. Cetak Tabel Perkalian 1-3 (Nested Loop)")
    print("5. Keluar")
    print("=" * 45)

    pilihan = input("Pilih menu (1-5): ")

    # ===================
    # MENU 5: KELUAR
    # ===================

    if pilihan == "5":
        print("Terima kasih telah menggunakan kalkulator ini.")
        print("Program selesai.")
        break

    # =========================================
    # MENU 1: OPERASI ARITMATIKA DASAR
    # =========================================

    elif pilihan == "1":
        print("\n== MENU OPERASI ARITMATIKA DASAR ==")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")

        op = input("Pilih operasi (1-4): ")

        if op not in ["1", "2", "3", "4"]:
            print("Peringatan: Pilihan operasi tidak valid.")
            input("\nTekan Enter untuk kembali ke menu utama...")
            continue

        try:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua  : "))
        except ValueError:
            print("Peringatan: Input harus berupa angka.")
            input("\nTekan Enter untuk kembali ke menu utama...")
            continue

        if op == "1":
            hasil = operasi3.tambah(a, b)
            print(f"Hasil penjumlahan {a:g} + {b:g} = {hasil:g}")

        elif op == "2":
            hasil = operasi3.kurang(a, b)
            print(f"Hasil pengurangan {a:g} - {b:g} = {hasil:g}")

        elif op == "3":
            hasil = operasi3.kali(a, b)
            print(f"Hasil perkalian {a:g} * {b:g} = {hasil:g}")

        elif op == "4":
            if b == 0:
                print("Peringatan: Pembagian dengan nol tidak diperbolehkan.")
            else:
                hasil = operasi3.bagi(a, b)
                print(f"Hasil pembagian {a:g} / {b:g} = {hasil:g}")

        input("\nTekan Enter untuk kembali ke menu utama...")

    # =========================================
    # MENU 2: CEK BILANGAN GANJIL/GENAP
    # =========================================

    elif pilihan == "2":
        print("\n== MENU CEK BILANGAN GANJIL/GENAP ==")

        try:
            angka = int(input("Masukkan angka bulat positif: "))
        except ValueError:
            print("Peringatan: Masukan harus berupa bilangan bulat.")
            input("\nTekan Enter untuk kembali ke menu utama...")
            continue

        if angka <= 0:
            print("Peringatan: Angka harus lebih dari 0.")
            input("\nTekan Enter untuk kembali ke menu utama...")
            continue

        status = operasi3.cek_ganjil_genap(angka)
        print(f"Hasil: Angka {angka} tergolong bilangan {status}")

        input("\nTekan Enter untuk kembali ke menu utama...")

    # ========================================
    # MENU 3: HITUNG DERET ARITMATIKA
    # ========================================

    elif pilihan == "3":
        print("\n== MENU HITUNG DERET ARITMATIKA ==")

        try:
            a = int(input("Suku pertama (a): "))
            b = int(input("Beda deret   (b): "))
        except ValueError:
            print("Peringatan: Suku pertama dan beda harus bilangan bulat.")
            input("\nTekan Enter untuk kembali ke menu utama...")
            continue

        # Memastikan banyak suku (n) berupa bilangan bulat positif
        while True:
            try:
                n = int(input("Banyak suku  (n): "))
            except ValueError:
                print("Peringatan: Banyak suku harus berupa bilangan bulat.")
                continue

            if n <= 0:
                print("Peringatan: Banyak suku (n) harus lebih dari 0.")
                continue

            break

        total_deret = operasi3.hitung_deret_aritmatika(a, b, n)
        print(f"Total jumlah seluruh deret aritmatika = {total_deret}")

        input("\nTekan Enter untuk kembali ke menu utama...")

    # ===============================================
    # MENU 4: TABEL PERKALIAN DENGAN NESTED LOOP
    # ===============================================

    elif pilihan == "4":
        print("\n== MENU TABEL PERKALIAN 1-3 (NESTED LOOP) ==")
        print("     1   2   3")

        for baris in range(1, 4):
            print(f"{baris}  |", end="")

            for kolom in range(1, 4):
                print(f"{baris * kolom:4}", end="")

            print()

        input("\nTekan Enter untuk kembali ke menu utama...")

    # ========================================
    # PILIHAN MENU TIDAK VALID
    # ========================================

    else:
        print("Peringatan: Pilihan menu tidak valid. Pilih antara 1-5.")
        input("\nTekan Enter untuk kembali ke menu utama...")