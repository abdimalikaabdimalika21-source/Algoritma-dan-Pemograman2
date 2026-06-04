def no1():
    print ('Hai namamu siapa?')
    anything = input()
    print ('Selamat ngoding', anything, '😁' )

def no2():
    anything = input('Ngoding pakai bahasa apa?')
    print ('wah ngoding pakai bahasa', anything, 'memang sangat menyenangkan' )

def no3():
    anything = input("Enter a number: ")
    something = anything ** 2.0
    print (anything, "to the power of 2 is", something)

def no4():
    anything = float(input('enter a mumber: '))
    something = anything ** 2.0
    print (anything, 'to the power of 2 is', something)

def no5():
    leg_a = float(input("input first leg length: "))
    leg_b = float(input("input second leg length: "))
    hypo = (leg_a**2 + leg_b**2) **.5
    print ("Hypotenuse length is", hypo)

def no6():
    leg_a = float(input("input first leg length: "))
    leg_b = float(input("input second leg length: "))
    print ("Hypotenuse length is", (leg_a**2 + leg_b**2) **.5)

def no7():
    fnam = input ("May I have your first name, please?")
    lnam = input ("May I have your last name, please?")
    print ("Thank you.")
    print ("\nYour name is " + fnam + " " + lnam + "." )

def no8():
    print ("+" + 10 * "-" + "+")
    print (("|" + " " * 10 + "|\n") * 5, end="")
    print ("+" + 10 * "-" + "+")

def no9():
    A = 20
    B = 13
    Nilai = A + B
    print ("Hasilnya = ", str(Nilai))

def no10():
    x = .5 * 5
    print ("Nilai X =", x)
    print (type(x))

def no11():
    a = float(input("Masukkan Nilai A ="))
    b = float(input("Masukkan Nilai B ="))
    print ("Hasil Penjumlahan =", a + b)
    print ("Hasil Pengurangan =", a - b)
    print ("Hasil Pembagian =", a / b)
    print ("Hasil Perkalian =", a * b)
    print ("Selamat kamu sudah pintar matematika")

def no12():
    x = float(input("Masukkan nilai x = "))
    y = 1.0 / (x + 1.0 / (x + 1.0 / (x + 1.0 / x)))
    print("Nilai y =", y)

def no13():
    jam = int(input("Waktu mulai (jam): "))
    menit = int(input("Waktu mulai (menit): "))
    durasi = int(input("Durasi Acara (menit): "))

    total_menit = menit + durasi
    jam += total_menit // 60
    menit = total_menit % 60

    jam = jam % 24  # agar tidak lebih dari 23

    print("Acara selesai pukul {:02d}:{:02d}".format(jam, menit))
