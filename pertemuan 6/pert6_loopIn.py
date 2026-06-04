def no1():
    while True:
        print("tidak akan berhenti  kecuali diinterupsi")

def no2():
    Nomer = 8
    while Nomer > 0:
        print("Nomer sekarang:", Nomer)
        Nomer -= 1

def no3():
    #membuat variabel angka ganjil dan genap
    angka_ganjil = 0
    angka_genap = 0

    #membaca angka pertama
    angka = int(input("Masukkan angka atau (0 untuk berhenti): "))
    while angka != 0:
        if angka % 2 == 0:
            angka_genap += 1
        else:
            angka_ganjil += 1
        angka = int(input("Masukkan angka atau (0 untuk berhenti): "))
    print("Jumlah angka genap:", angka_genap)
    print("Jumlah angka ganjil:", angka_ganjil)

def no4():
    secret_number = 67

    print(
    """
    +===========================================+
    | Selamat datang di game saya, muggle!      |
    | masukan suatu angka dan tebak             |
    | angka berapa yang saya pilih              |
    | untuk kamu.                               |
    | jadi, berapa angka rahasianya?            |
    +===========================================+
    """)

    angka = int(input("Masukkan angka tebakanmu: "))
    while angka != secret_number:
        print("Hahaha ! kamu nyangkut deh di Loop saya.")
        angka = int(input("Masukkan angka tebakanmu: "))
    print("Selamat, Muggle! kamu bebas sakarang!")    

def no5():
    for a in range(10):
        print("nilai a saat ini adalah", a)
    for b in range(2, 8):
        print("nilai b saat ini adalah", b)
    for c in range(2, 8, 3):
        print("nilai c saat ini adalah", c)
    for d in range(1, 1):
        print("nilai d saat ini adalah", d)
    for e in range(2, 1):
        print("nilai e saat ini adalah", e)

def no6():
    power = 1
    for exponent in range(16):
        print("2 pangkat", exponent, "adalah", power)
        power *= 2

def no7():
    # contoh Break
    print("Intruksi break:")
    for i in range(1, 10):
        if i == 5:
            break
        print("Bagian ini ada di dalam loop:", i)
    print("Bagian ini ada di luar loop")
    
    # contoh Continue
    print("\nIntruksi continue:")
    for i in range(1, 10):
        if i == 5:
            continue
        print("Bagian ini ada di dalam loop:", i)
    print("Bagian ini ada di luar loop")

def no8():
    secret_number = 23
    print(
    """
    +===========================================+
    | Selamat datang di game saya, muggle!      |
    | masukan suatu angka dan tebak             |
    | angka berapa yang saya pilih              |
    | untuk kamu.                               |
    | jadi, berapa angka rahasianya?            |
    +===========================================+
    """)
    while True:
        angka = int(input("Masukkan angka tebakanmu: "))
        if angka == secret_number:
            print("Selamat, Muggle! kamu bebas sakarang!")
            break #loop berhenti jika tebakan benar
        else:
            print("Hahaha ! kamu nyangkut deh di Loop saya.")

def no9():
    kata = input("masukan kata: ").upper()
    for huruf in kata:
        if huruf == "A":
            continue
        elif huruf == "I":
            continue
        elif huruf == "U":
            continue
        elif huruf == "E":
            continue
        elif huruf == "O":
            continue
        else:
            print(huruf)

def no10():
    i = 1
    while i < 5:
        print(i)
        i += 1
    else:
        print("else:", i)

def no11():
    for i in range(5):
        print(i)
    else:
        print("else:", i)

    i=111
    for i in range(2,1):
        print(i)
    else:
        print("else:", i)

def no12():
    a = (1 > 0)
    b = (1 < 0)

    x = (a and b) or (a and not b)
    print(x)
    y = (not a or b) and (a or b)
    print(y)

def no13():
    i= 15
    j= 22

    log= i and j
    print(log)

    bit= i & j
    print(bit)

    logneg= not i
    print(logneg)

    bitneg= ~i
    print(bitneg)

def no14():
    a = 5
    a_right = a >> 1
    a_left = a << 1
    print(a, a_right, a_left)

def no15():
    x=4
    y=1

    a= x & y
    b= x | y
    c= ~x
    d= x ^ 5
    e= x >> 2
    f= x << 2

    print(a, b, c, d, e, f)




