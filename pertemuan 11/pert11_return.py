from numpy import insert


def no1():
    def selamat_ulang_tahun(harapan=True):
        print("Tiga...")
        print("Dua...")
        print("Satu...")
        if not harapan:
            return
        
        print("Selamat ulang tahun!")
    selamat_ulang_tahun() #pemanggilan tanpa argumen, harapan bernilai True

def no2():
       def selamat_ulang_tahun(harapan=True):
        print("Tiga...")
        print("Dua...")
        print("Satu...")
        if not harapan:
            return
        
        print("Selamat ulang tahun!")
       selamat_ulang_tahun(False) #pemanggilan dengan argumen False, harapan bernilai False

def no3():
    def fungsi_malas():
        return 123
    
    x = fungsi_malas()
    print("Hasil dari fungsi malas adalah:", x)

def no4():
    def fungsi_malas():
        print("aku lagi mode malas")
        return 123
    
    print("Mata kuliah ini seru banget!")
    fungsi_malas()
    print("Mata kuliah ini sangat bosan...")

def no5():
    def fungsi_aneh(n):
        if (n % 2 == 0):
            return True
        
    print(fungsi_aneh(14))
    print(fungsi_aneh(15))

def no6():
    def penjumlahan_list(lst):
        s = 0

        for elemen in lst:
            s += elemen
        return s

    print(penjumlahan_list([10, 15, 20 ]))

def no7():
    def penjumlahan_list(lst):
        s = 0

        for elemen in lst:
            s += elemen
        return s

    print(penjumlahan_list(7))

def no8():
    def fungsi_list_aneh(n):
        list_aneh = []

        for i in range(0, n):
            list_aneh.insert(0, i)
            
        return list_aneh
        
    print(fungsi_list_aneh(5))

def no9():
    def tahun_kabisat(tahun):
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            return True
        else:
            return False

    data_uji =[1900, 2000, 2016, 1987]
    data_hasil = [False, True, True, False]

    for i in range(len(data_uji)):
        th = data_uji[i]
        print(th,"->", end="")
        hasil = tahun_kabisat(th)
        if hasil == data_hasil[i]:
            print("ok")
        else:
            print("gagal")

def no10():
    def tahun_kabisat(tahun):
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            return True
        else:
            return False
        
    def hari_didalam_bulan(tahun, bulan):
        hari_dalam_bulan = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if bulan == 2 and tahun_kabisat(tahun):
            return 29
        else:
            return hari_dalam_bulan[bulan]

    data_uji =[1900, 2000, 2016, 1987]
    data_bulan = [2,2,1,11]
    data_hasil = [28,29,31,30]

    for i in range(len(data_uji)):
        th = data_uji[i]
        bln = data_bulan[i]
        print(th, bln, "->", end="")
        hasil = hari_didalam_bulan(th, bln)
        if hasil == data_hasil[i]:
            print("ok")
        else:
            print("gagal")

def no11():
     def tahun_kabisat(tahun):
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            return True
        else:
            return False

     def hari_didalam_bulan(tahun, bulan):
        if bulan in [4,6,9,11]:
            return 30
        elif bulan == 2:
            return 29 if tahun_kabisat(tahun) else 28
        else:
            return 31
        
     def hari_pada_tahun(tahun, bulan, hari):
         total = 0
         #loop buat nambahin jumlah hari di bulan-bulan sebelumnya
         for b in range(1, bulan):
             total += hari_didalam_bulan(tahun, b)
         total += hari
         return total
     
     print(hari_pada_tahun(2000, 12, 31))

def no12():
    def cek_prima(bilangan):
        if bilangan <= 1:
            return False
        for i in range(2, bilangan):
            if bilangan % i == 0:
                return False
        return True
    
    for i in range(1, 20):
        if cek_prima(i + 1):
            print(i + 1, end=" ")
    print()

def no13():
    def Liter100km_ke_mpg(liter):
        galon = liter / 3.785411784
        mill = 100000 / 1609.344
        return mill / galon
    
    def Mpg_ke_Liter100km(mpg):
        liter = 3.785411784
        km100 = (mpg * 1609.344) / 100000
        return liter / km100
    
    print(Liter100km_ke_mpg(3.9))
    print(Liter100km_ke_mpg(7.5))
    print(Liter100km_ke_mpg(10.0))
    print(Mpg_ke_Liter100km(60.3))
    print(Mpg_ke_Liter100km(31.4))
    print(Mpg_ke_Liter100km(23.5))

no13()