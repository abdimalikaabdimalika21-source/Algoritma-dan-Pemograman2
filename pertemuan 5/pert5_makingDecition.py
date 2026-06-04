def no1():
    x = 0
    y = 1
    z = 0
    print(x==y)
    print(x!=y)
    print(x<y)
    print(y>z)
    print(z<=x)
    print(x>=y)

def no2():
    n = int(input("masukkan nilai n = "))
    if n > 100:
        print(True)
    else:
        print(False)

def no3():
    x = 18

    if x > 8:   # kondisi
        print ("x lebih besar dari 8")

def no4():
    x = 18

    if x > 8:   # kondisi 1
        print ("x lebih besar dari 8")

        if x < 20:  # kondisi 2
            print ("x lebih kecil dari 20")

        if x == 18:  # kondisi 3
            print ("x sama dengan 18")

def no5():
    x = 15

    if x > 10:
        print("x lebih besar dari 10")
        
    else:
        print("x tidak lebih besar dari 10")

def no6():
    x = float(input("Masukkan nilai x: "))

    if x == 10:
        print("x sama dengan 10")

    elif x > 10:
        print("x lebih besar dari 10")

    elif x < 10:
        print("x lebih kecil dari 10")

    elif x >= 10:
        print("x lebih besar atau sama dengan 10")

    else:
        print("x tidak lebih besar dari 10")

def no7():
    angka_ke1 = int(input("masukkan angka pertama: "))
    angka_ke2 = int(input("masukkan angka kedua: "))

    if angka_ke1 > angka_ke2:
        angka_besar  = angka_ke1
    else:
        angka_besar  = angka_ke2

    print("angka yang lebih besar adalah: ", angka_besar)

def no8():
    angka_ke1 = float(input("masukkan angka pertama: "))
    angka_ke2 = float(input("masukkan angka kedua: "))
    angka_ke3 = float(input("masukkan angka ketiga: "))

    if angka_ke1 > angka_ke2 and angka_ke1 > angka_ke3:
        angka_besar = angka_ke1

    elif angka_ke2 > angka_ke3 and angka_ke2 > angka_ke1:
        angka_besar = angka_ke2

    else:
        angka_besar = angka_ke3

    print("angka yang paling besar adalah: ", angka_besar)

def no9():
    angka_ke1 = float(input("masukkan angka pertama: "))
    angka_ke2 = float(input("masukkan angka kedua: "))
    angka_ke3 = float(input("masukkan angka ketiga: "))

    angka_besar = max(angka_ke1, angka_ke2, angka_ke3)

    print("angka yang paling besar adalah: ", angka_besar)

def no10():
    pendapatan = float(input("Masukkan pendapatan bulanan Anda: "))
    pajak = 0

    # Mengubah pendapatan bulanan menjadi tahunan
    pendapatan_tahun = pendapatan * 12

    if pendapatan_tahun <= 60000000:
        pajak = pendapatan_tahun * 0.05
    elif pendapatan_tahun <= 250000000:
        pajak = pendapatan_tahun * 0.15
    elif pendapatan_tahun <= 500000000:
        pajak = pendapatan_tahun * 0.25
    else:
        pajak = pendapatan_tahun * 0.30

    print("Pajak penghasilan yang harus anda bayar adalah", pajak, "rupiah")