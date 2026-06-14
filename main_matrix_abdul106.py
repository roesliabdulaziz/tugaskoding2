import abdul106


def garis():
    print("=" * 70)


def tampilkan_data_awal(A, B):
    garis()
    print("PROGRAM OPERASI MATRIKS 3x3")
    print("Nama modul: abdul106.py")
    print("Cara panggil: import abdul106, lalu abdul106.nama_fungsi()")
    garis()
    abdul106.cetak_matriks(A, "Matriks A:")
    abdul106.cetak_matriks(B, "Matriks B:")


def demo_operasi_umum():
    A = [
        [2, 1, 3],
        [1, 0, 2],
        [4, 1, 8],
    ]

    B = [
        [1, 2, 0],
        [0, 1, 3],
        [2, 0, 1],
    ]

    tampilkan_data_awal(A, B)

    abdul106.cetak_matriks(abdul106.penjumlahan(A, B), "1. Penjumlahan A + B:")
    abdul106.cetak_matriks(abdul106.pengurangan(A, B), "2. Pengurangan A - B:")
    abdul106.cetak_matriks(abdul106.perkalian_skalar(A, 3), "3. Perkalian skalar 3 x A:")
    abdul106.cetak_matriks(abdul106.perkalian_matriks(A, B), "4. Perkalian matriks A x B:")
    abdul106.cetak_matriks(abdul106.transpose(A), "5. Transpose A:")

    print("6. Determinan A:", abdul106.determinan(A))
    print("7. Minor A posisi baris 0 kolom 0:", abdul106.nilai_minor(A, 0, 0))
    print("8. Kofaktor A posisi baris 0 kolom 0:", abdul106.kofaktor(A, 0, 0))
    print()

    abdul106.cetak_matriks(abdul106.matriks_minor(A), "9. Matriks minor A:")
    abdul106.cetak_matriks(abdul106.matriks_kofaktor(A), "10. Matriks kofaktor A:")
    abdul106.cetak_matriks(abdul106.adjoin(A), "11. Adjoin / adjugate A:")
    abdul106.cetak_matriks(abdul106.invers(A), "12. Invers A:")

    print("13. Rank A:", abdul106.rank(A))
    print()

    abdul106.cetak_matriks(abdul106.tukar_baris(A, 0, 1), "14a. Operasi baris: tukar baris 0 dan 1:")
    abdul106.cetak_matriks(abdul106.kali_baris(A, 0, 2), "14b. Operasi baris: baris 0 dikali 2:")
    abdul106.cetak_matriks(
        abdul106.tambah_kelipatan_baris(A, 2, 0, -2),
        "14c. Operasi baris: baris 2 ditambah -2 kali baris 0:",
    )

    abdul106.cetak_matriks(abdul106.eliminasi_gauss(A), "15. Reduksi baris / eliminasi Gauss A:")

    D = [
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3],
    ]
    abdul106.cetak_matriks(D, "Matriks D untuk contoh eigen:")
    print("16. Polinom karakteristik D:", abdul106.polinom_karakteristik(D))
    print("17. Nilai eigen D:", abdul106.nilai_eigen(D))
    print("18. Vektor eigen untuk lambda = 2:", abdul106.vektor_eigen(D, 2))
    print()


def input_matriks_3x3(nama):
    print(f"Masukkan matriks {nama} ukuran 3x3.")
    print("Contoh input satu baris: 1 2 3")
    hasil = []
    for i in range(3):
        while True:
            data = input(f"Baris {i + 1}: ").strip().split()
            if len(data) != 3:
                print("Input harus berisi 3 angka.")
                continue
            try:
                hasil.append([float(nilai) for nilai in data])
                break
            except ValueError:
                print("Semua input harus angka.")
    return abdul106.rapikan_matriks(hasil)


def menu_interaktif():
    A = input_matriks_3x3("A")

    while True:
        garis()
        print("MENU OPERASI MATRIKS 3x3")
        garis()
        print("1. Penjumlahan dengan matriks B")
        print("2. Pengurangan dengan matriks B")
        print("3. Perkalian skalar")
        print("4. Perkalian dengan matriks B")
        print("5. Transpose")
        print("6. Determinan")
        print("7. Minor dan kofaktor")
        print("8. Adjoin")
        print("9. Invers")
        print("10. Rank")
        print("11. Eliminasi Gauss")
        print("12. Nilai eigen")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        try:
            if pilihan == "1":
                B = input_matriks_3x3("B")
                abdul106.cetak_matriks(abdul106.penjumlahan(A, B), "A + B:")
            elif pilihan == "2":
                B = input_matriks_3x3("B")
                abdul106.cetak_matriks(abdul106.pengurangan(A, B), "A - B:")
            elif pilihan == "3":
                skalar = float(input("Masukkan skalar: "))
                abdul106.cetak_matriks(abdul106.perkalian_skalar(A, skalar), "Hasil perkalian skalar:")
            elif pilihan == "4":
                B = input_matriks_3x3("B")
                abdul106.cetak_matriks(abdul106.perkalian_matriks(A, B), "A x B:")
            elif pilihan == "5":
                abdul106.cetak_matriks(abdul106.transpose(A), "Transpose A:")
            elif pilihan == "6":
                print("Determinan A:", abdul106.determinan(A))
            elif pilihan == "7":
                baris = int(input("Baris yang dihapus (0/1/2): "))
                kolom = int(input("Kolom yang dihapus (0/1/2): "))
                print("Minor:", abdul106.nilai_minor(A, baris, kolom))
                print("Kofaktor:", abdul106.kofaktor(A, baris, kolom))
            elif pilihan == "8":
                abdul106.cetak_matriks(abdul106.adjoin(A), "Adjoin A:")
            elif pilihan == "9":
                abdul106.cetak_matriks(abdul106.invers(A), "Invers A:")
            elif pilihan == "10":
                print("Rank A:", abdul106.rank(A))
            elif pilihan == "11":
                abdul106.cetak_matriks(abdul106.eliminasi_gauss(A), "Eliminasi Gauss A:")
            elif pilihan == "12":
                print("Nilai eigen real bulat/sederhana A:", abdul106.nilai_eigen(A))
            elif pilihan == "0":
                print("Program selesai.")
                break
            else:
                print("Pilihan tidak tersedia.")
        except Exception as error:
            print("Terjadi kesalahan:", error)


if __name__ == "__main__":
    demo_operasi_umum()
    jawab = input("mau coba ndili? (y/t): ").strip().lower()
    if jawab == "y":
        menu_interaktif()
