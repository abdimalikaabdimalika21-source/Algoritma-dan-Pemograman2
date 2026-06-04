def no1():
    angka = [1,2,3,4,5]
    print("Ini List Awal: ", angka) 

    angka[0] = 222
    print("ini list Baru: ", angka)

def no2():
    angka = [10,20,30,40,50]

    print ("Ini Angka Awal atau 0")
    print (angka[0])
    print ("Ini Seluruh Angka")
    print (angka)

def no3():
    list = [10,20,30,40,50]

    print ( "divariabel list ada", len(list), "angka")

def no4():
    angka = [1,2,3,4,5]
    del angka [1]

    print (len(angka))
    print (angka)

def no5():
    angka = [4, 3, 6, 2, 1]
    print(angka[-1]) #mengakses angka pada index -1

def no6():
    angka_list = [1, 2, 3, 4, 5]

    nilai_baru = int(input("Masukkan angka untuk mengganti bagian tengah: "))
    angka_list[2] = nilai_baru

    del angka_list[-1]

    print("Jumlah elemen sekarang:", len(angka_list))
    print(angka_list)

def no7():
    angka = [100, 7, 2, 1]
    print(len(angka))
    print(angka)

    angka.append(4)
    print(len(angka))
    print(angka)

    angka.insert(0, 222)
    print(len(angka))
    print(angka)

    angka.insert(1, 333)
    print(len(angka))
    print(angka)

def no8():
    my_list=[]

    for i in range(5):
        my_list.append(i+1)

    print(my_list)


def no9():
    my_list=[]

    for i in range(5):
        my_list.insert(0,i+1)
    print(my_list)

def no10():
    my_list = [10,1,8,3,5]
    total = 0

    for i in range (len(my_list)):
        total += my_list[i]

    print(total)   

def no11():
    my_list = [10,1,8,3,5]
    total = 0

    for i in range (len(my_list)):
        total += i

    print(total)
no11()

def no12():
    my_List = [10, 1, 8, 3, 5]

    my_List[0], my_List[4] = my_List[4], my_List[0]
    my_List[1], my_List[3] = my_List[3], my_List[1]

    print(my_List)

    length = len(my_List)

    for i in range(length // 2):
        my_List[i], my_List[length - i - 1] = my_List[length - i - 1], my_List[i]

        print(my_List)


def no13():
    #Exo merupakan grup vokal asal korea selatan beranggotakan 9 orang: Suho, Kai, Chanyeol, Sehun, DO, Baekhyun, Xiumin, Lay dan Chen.
    #Langkah 1: buatlah sebuat list kosong dengan nama exo
    #Langkah 2: gunakan method append( ) untuk menambahkan anggota:Suho, Kai, Chanyeol dan Sehun.
    #Langkah 3: gunakan for untuk menambahkan anggota: DO, Baekhyun, Kris, Lay, Luhan, Tao, dan Chen.
    #Langkah 4: Hapuslah anggota: Kris, Luhan dan Tao
    #Langkah 5: gunakan method insert() untuk menambahkan anggota Xiumin pada elemen ke tiga dari terakhir

    exo = []

    print("Langkah 1:", exo)

    exo.append("Suho")
    exo.append("Kai")
    exo.append("Chanyeol")
    exo.append("Sehun")

    print("Langkah 2:", exo)

    anggota_baru = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
    for anggota in anggota_baru:
        exo.append(anggota)

    print("Langkah 3:", exo)

    exo.remove("Kris")
    exo.remove("Luhan")
    exo.remove("Tao")

    print("Langkah 4:", exo)

    exo.insert(-2, "Xiumin")

    print("Langkah 5:", exo)

    print("Jumlah anggota exo:", len(exo))
