def no1():    
    pangkat = [x ** 2 for x in range(10)]
    print(pangkat)
    pangkat_dua = [2 ** i for i in range(16)]
    print(pangkat_dua)
    ganjil = [x for x in pangkat if x % 2 == 1]
    print(ganjil)

def no2():
    papan_catur = []
    KOSONG = "-"
    BENTENG = "B"
    KUDA = "K"
    for i in range(8):
        baris = [KOSONG for i in range(8)]
        papan_catur.append(baris)
    
    papan_catur[0][0] = BENTENG
    papan_catur[0][7] = BENTENG
    papan_catur[7][0] = BENTENG
    papan_catur[7][7] = BENTENG

    papan_catur[0][1] = KUDA
    papan_catur[0][6] = KUDA
    papan_catur[7][1] = KUDA
    papan_catur[7][6] = KUDA

    for baris in papan_catur:
        print(baris)

def no3():
    # Membuat struktur: 3 gedung, 15 lantai, 20 kamar
    kamar = [[[False for k in range(20)] for i in range(15)] for g in range(3)]

    # Contoh mengisi beberapa kamar (True = terisi)
    kamar[1][9][13] = True   # gedung 2, lantai 10, kamar 14
    kamar[0][4][1] = True    # gedung 1, lantai 5, kamar 2

    # Menghitung kamar kosong di gedung 2 lantai 10
    tersedia = 0

    for no_kamar in range(20):
        if not kamar[1][9][no_kamar]:  # gedung 2 (1), lantai 10 (9)
            tersedia += 1

    print(f"Kamar tersedia di gedung 2 lantai 10: {tersedia}")

def no4():
    def pesan(angka):
        print("Anda memasukkan angka", angka)

    angka=123
    pesan(5)
    print(angka)

def no5():
    # Membuat list bilangan 1 sampai 10
    angka = [x for x in range(1, 11)]

    # Mengambil bilangan genap lalu dikalikan 3
    hasil = [x * 3 for x in angka if x % 2 == 0]

    print("Bilangan 1-10:", angka)
    print("Hasil bilangan genap x 3:", hasil)

def no6():
    # Membuat array 2 dimensi 3x3 berisi angka 1 sampai 9
    array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

    # Menampilkan seluruh isi array
    for baris in array:
        print(baris)

def no7():
    data = [[2,4],[6,8],[10,12]]
    flatten = [x for sublist in data for x in sublist]
    print(flatten)

def no8():
    # Fungsi menghitung luas persegi panjang
    def luas_persegi_panjang(panjang, lebar):
        return panjang * lebar

    # Memanggil fungsi
    hasil = luas_persegi_panjang(8, 5)

    print("Luas persegi panjang =", hasil)


