
EPSILON = 1e-9


def validasi_matriks_3x3(A):
    if not isinstance(A, list) or len(A) != 3:
        raise ValueError("Matriks harus berupa list 2 dimensi berukuran 3x3.")
    for baris in A:
        if not isinstance(baris, list) or len(baris) != 3:
            raise ValueError("Setiap baris matriks harus memiliki tepat 3 elemen.")
        for nilai in baris:
            if not isinstance(nilai, (int, float)):
                raise TypeError("Semua elemen matriks harus berupa angka.")
    return True


def salin_matriks(A):
    validasi_matriks_3x3(A)
    return [baris[:] for baris in A]


def rapikan_angka(nilai):
    if isinstance(nilai, float):
        if abs(nilai) < EPSILON:
            return 0
        nilai = round(nilai, 10)
        bulat = round(nilai)
        if abs(nilai - bulat) < EPSILON:
            return int(bulat)
    return nilai


def rapikan_matriks(A):
    return [[rapikan_angka(nilai) for nilai in baris] for baris in A]


def cetak_matriks(A, judul=None):
    validasi_matriks_3x3(A)
    if judul:
        print(judul)
    for baris in A:
        print("[ " + "  ".join(f"{rapikan_angka(nilai):>10}" for nilai in baris) + " ]")
    print()


def identitas_3x3():
    return [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]


def penjumlahan(A, B):
    validasi_matriks_3x3(A)
    validasi_matriks_3x3(B)
    return [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]


def pengurangan(A, B):
    validasi_matriks_3x3(A)
    validasi_matriks_3x3(B)
    return [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]


def perkalian_skalar(A, skalar):
    validasi_matriks_3x3(A)
    if not isinstance(skalar, (int, float)):
        raise TypeError("Skalar harus berupa angka.")
    return [[A[i][j] * skalar for j in range(3)] for i in range(3)]


def perkalian_matriks(A, B):
    validasi_matriks_3x3(A)
    validasi_matriks_3x3(B)
    hasil = [[0, 0, 0] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            total = 0
            for k in range(3):
                total += A[i][k] * B[k][j]
            hasil[i][j] = total
    return hasil


def transpose(A):
    validasi_matriks_3x3(A)
    return [[A[i][j] for i in range(3)] for j in range(3)]


def determinan_2x2(M):
    if len(M) != 2 or len(M[0]) != 2 or len(M[1]) != 2:
        raise ValueError("Determinan 2x2 membutuhkan matriks berukuran 2x2.")
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def determinan(A):
    validasi_matriks_3x3(A)
    positif = (
        A[0][0] * A[1][1] * A[2][2]
        + A[0][1] * A[1][2] * A[2][0]
        + A[0][2] * A[1][0] * A[2][1]
    )
    negatif = (
        A[0][2] * A[1][1] * A[2][0]
        + A[0][0] * A[1][2] * A[2][1]
        + A[0][1] * A[1][0] * A[2][2]
    )
    return rapikan_angka(positif - negatif)


def minor(A, baris_hapus, kolom_hapus):
    validasi_matriks_3x3(A)
    if baris_hapus not in range(3) or kolom_hapus not in range(3):
        raise IndexError("Indeks baris dan kolom harus 0, 1, atau 2.")
    return [
        [A[i][j] for j in range(3) if j != kolom_hapus]
        for i in range(3)
        if i != baris_hapus
    ]


def nilai_minor(A, baris, kolom):
    return determinan_2x2(minor(A, baris, kolom))


def kofaktor(A, baris, kolom):
    tanda = (-1) ** (baris + kolom)
    return tanda * nilai_minor(A, baris, kolom)


def matriks_minor(A):
    validasi_matriks_3x3(A)
    return [[nilai_minor(A, i, j) for j in range(3)] for i in range(3)]


def matriks_kofaktor(A):
    validasi_matriks_3x3(A)
    return [[kofaktor(A, i, j) for j in range(3)] for i in range(3)]


def adjoin(A):
    return transpose(matriks_kofaktor(A))


def invers(A):
    det = determinan(A)
    if abs(det) < EPSILON:
        raise ValueError("Matriks singular, sehingga invers tidak ada.")
    adj = adjoin(A)
    return rapikan_matriks(perkalian_skalar(adj, 1 / det))


def tukar_baris(A, baris1, baris2):
    M = salin_matriks(A)
    M[baris1], M[baris2] = M[baris2], M[baris1]
    return M


def kali_baris(A, baris, skalar):
    if abs(skalar) < EPSILON:
        raise ValueError("Skalar tidak boleh nol.")
    M = salin_matriks(A)
    M[baris] = [nilai * skalar for nilai in M[baris]]
    return M


def tambah_kelipatan_baris(A, target, sumber, skalar):
    M = salin_matriks(A)
    M[target] = [M[target][j] + skalar * M[sumber][j] for j in range(3)]
    return M


def eliminasi_gauss(A):
    validasi_matriks_3x3(A)
    M = [[float(nilai) for nilai in baris] for baris in A]
    baris_pivot = 0

    for kolom in range(3):
        pivot = None
        for r in range(baris_pivot, 3):
            if abs(M[r][kolom]) > EPSILON:
                pivot = r
                break

        if pivot is None:
            continue

        M[baris_pivot], M[pivot] = M[pivot], M[baris_pivot]
        nilai_pivot = M[baris_pivot][kolom]

        for r in range(baris_pivot + 1, 3):
            faktor = M[r][kolom] / nilai_pivot
            for c in range(kolom, 3):
                M[r][c] -= faktor * M[baris_pivot][c]

        baris_pivot += 1
        if baris_pivot == 3:
            break

    return rapikan_matriks(M)


def rref(A):
    validasi_matriks_3x3(A)
    M = [[float(nilai) for nilai in baris] for baris in A]
    baris_pivot = 0

    for kolom in range(3):
        pivot = None
        for r in range(baris_pivot, 3):
            if abs(M[r][kolom]) > EPSILON:
                pivot = r
                break

        if pivot is None:
            continue

        M[baris_pivot], M[pivot] = M[pivot], M[baris_pivot]
        nilai_pivot = M[baris_pivot][kolom]
        for c in range(3):
            M[baris_pivot][c] /= nilai_pivot

        for r in range(3):
            if r != baris_pivot:
                faktor = M[r][kolom]
                for c in range(3):
                    M[r][c] -= faktor * M[baris_pivot][c]

        baris_pivot += 1
        if baris_pivot == 3:
            break

    return rapikan_matriks(M)


def rank(A):
    hasil_rref = rref(A)
    jumlah = 0
    for baris in hasil_rref:
        if any(abs(nilai) > EPSILON for nilai in baris):
            jumlah += 1
    return jumlah


def polinom_karakteristik(A):
    validasi_matriks_3x3(A)
    tr = A[0][0] + A[1][1] + A[2][2]
    A2 = perkalian_matriks(A, A)
    tr_A2 = A2[0][0] + A2[1][1] + A2[2][2]
    det = determinan(A)
    koef_lambda2 = -tr
    koef_lambda = (tr * tr - tr_A2) / 2
    konstanta = -det
    return [
        1,
        rapikan_angka(koef_lambda2),
        rapikan_angka(koef_lambda),
        rapikan_angka(konstanta),
    ]


def nilai_polinom(koefisien, x):
    hasil = 0
    for koef in koefisien:
        hasil = hasil * x + koef
    return hasil


def nilai_eigen(A, batas=100):
    koef = polinom_karakteristik(A)
    hasil = []
    for x in range(-batas, batas + 1):
        if abs(nilai_polinom(koef, x)) < EPSILON:
            hasil.append(x)
    return hasil


def ruang_null(M):
    R = rref(M)
    pivot = []
    for i in range(3):
        for j in range(3):
            if abs(R[i][j]) > EPSILON:
                pivot.append((i, j))
                break

    kolom_pivot = [kolom for _, kolom in pivot]
    kolom_bebas = [j for j in range(3) if j not in kolom_pivot]

    if not kolom_bebas:
        return []

    basis = []
    for bebas in kolom_bebas:
        v = [0, 0, 0]
        v[bebas] = 1
        for baris, kolom in pivot:
            v[kolom] = -R[baris][bebas]
        basis.append([rapikan_angka(nilai) for nilai in v])
    return basis


def vektor_eigen(A, lamda):
    validasi_matriks_3x3(A)
    I = identitas_3x3()
    lamda_I = perkalian_skalar(I, lamda)
    A_kurang_lamda_I = pengurangan(A, lamda_I)
    return ruang_null(A_kurang_lamda_I)

determinan_3x3 = determinan
minor_matriks = matriks_minor
kofaktor_matriks = matriks_kofaktor
adjoin_matriks = adjoin
invers_matriks = invers
reduksi_baris = eliminasi_gauss
