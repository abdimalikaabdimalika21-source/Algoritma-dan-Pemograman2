def no1():
    def penjumlahan(x):
        bilangan = 7
        return x + 7
    
    print(penjumlahan(4))
    print(penjumlahan(10))

def no2():
    bilangan = 2
    def penjumlahan(x):
        return x + bilangan
    print(penjumlahan(7))

def no3():
    def perkalian(x):
        return x * bilangan
    bilangan = 5
    print(perkalian(3))

def no4():
    bilangan = 2
    print(bilangan) #output: 2
    def return_bilangan():
        global bilangan
        bilangan = 5
        return bilangan
    print(return_bilangan()) 
    print(bilangan) 

def no5():
    def hitung_imt(berat, tinggi):
        imt = float(berat) / (float(tinggi) * float(tinggi))
        return imt

    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (m): "))


    index_masa_tubuh = hitung_imt(berat, tinggi)
    kategori = ["Normal", "Gemuk", "Obesitas"]


    # kategori IMT yang di dapat
    if index_masa_tubuh >= 18.5 and index_masa_tubuh < 25:
        print("Index Masa Tubuh anda adalah:", index_masa_tubuh, "Termasuk kategori:", kategori[0])
    elif index_masa_tubuh >= 25 and index_masa_tubuh < 27:
        print("Index Masa Tubuh anda adalah:", index_masa_tubuh, "Termasuk kategori:", kategori[1])
    else:
        print("Index Masa Tubuh anda adalah:", index_masa_tubuh, "Termasuk kategori:", kategori[2])

def no6():
    def cek_segitiga(a,b,c):
        if a + b <= c:
            return False
        if b + c <= a:
            return False
        if a + c <= b:
            return False
        return True
    print(cek_segitiga(1,1,1))
    print(cek_segitiga(1,1,3))

def no7():
    def cek_segitiga(a,b,c):
        if a + b <= c or b + c <= a or a + c <= b:
            return False
        return True
    print(cek_segitiga(1,1,1))
    print(cek_segitiga(1,1,3))

def no8():
    def cek_segitiga(a,b,c):
        return a + b > c and b + c > a and a + c > b
    print(cek_segitiga(1,1,1))
    print(cek_segitiga(1,1,3))

def no9():
    def faktorial(n):
        if n < 0:
            return None
        if n < 2:
            return 1
    
        hasil = 1 
        for i in range(2, n + 1): 
            hasil *= i 
        return hasil
    n = int(input("Masukkan nilai yang ingin di faktorialkan: "))
    print(str(n) + "! =", faktorial(n))

def no10():
    # penjumlahan dari dua bilangan sebelumnya, dimulai dengan 0 dan 1
    def fibonacci(n):
        if n < 1:
            return None
        if n < 3:
            return 1
        
        elem_1 = elem_2 = 1 # inisialisasi nilai untuk elemen pertama dan kedua dalam deret Fibonacci
        hasil_jumlah = 0 # variabel untuk menyimpan hasil penjumlahan dari dua elemen sebelumnya
        for i in range(3, n + 1): # iterasi mulai dari elemen ke-3 hingga
            hasil_jumlah = elem_1 + elem_2 # hitung jumlah dari dua elemen sebelumnya
            elem_1, elem_2 = elem_2, hasil_jumlah # update nilai elemen pertama dan kedua untuk iterasi berikutnya
        return elem_2 # elem_2 akan menjadi nilai Fibonacci ke-n setelah loop selesai

    for n in range(1, 10):
        print(n, "->", fibonacci(n))

def no11():
    def faktorial_rekursif(n):
        if n < 0:
            return None
        if n < 2:
            return 1
        return n * faktorial_rekursif(n-1)

    n = int(input("Masukkan nilai yang ingin di faktorialkan: "))
    print(str(n) + "! =", faktorial_rekursif(n))

def no12():
    def fibonacci_rekursif(n):
        if n < 1:
            return None
        if n < 3:
            return 1
        return fibonacci_rekursif(n - 1) + fibonacci_rekursif(n - 2)

    for n in range(1, 10):
        print(n, "->", fibonacci_rekursif(n))

