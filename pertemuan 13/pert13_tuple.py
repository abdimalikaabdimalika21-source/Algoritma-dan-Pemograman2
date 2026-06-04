def no1():
    #membuat tuple
    my_tuple = (1, 2, 3, 4, 5)
    print(my_tuple)

def no2():
    my_tuple =(1, 10, 100, 1000)

    print(my_tuple[0])
    print(my_tuple[-1])
    print(my_tuple[1:])
    print(my_tuple[:-2])

    for element in my_tuple:
        print(element)

def no3():
    my_tuple =(1, 10, 100, 1000)

    my_tuple.append(10000)
    del my_tuple[0]
    my_tuple[1] = -10

    print(my_tuple)

def no4():
    my_tuple = (1, 10, 100, 1000)
    t1 = my_tuple + (10000, 100000)
    t2 = my_tuple * 3

    print(len(t2))
    print(t1)
    print(t2)
    print(10 in my_tuple)
    print(-10 not in my_tuple)

def no5():
    #simultan pada tuple
    a, b, c = (1, 2, 3)
    
    var= 1, 2, 3
    t1 = (1, )
    t2 = (2, )
    t3 = (3, var)
    t1, t2, t3= t2, t3, t1
    print(t1, t2, t3)

def no6(): 
    dictionary = {"nama": "Alice", "umur": 30, "kota": "Jakarta"}
    banyak_siswa = {"kelas A": 25, "kelas B": 30, "kelas C": 28}
    dictionary_kosong = {}

    print(dictionary)
    print(banyak_siswa)
    print(dictionary_kosong)

def no7():
    dictionary = {"nama": "Alice", "umur": 30, "kota": "Jakarta"}
    banyak_siswa = {"kelas A": 25, "kelas B": 30, "kelas C": 28}
    dictionary_kosong = {}

    print(dictionary["nama"])
    print(banyak_siswa["kelas A"])

def no8():
    dictionary = {"nama": "Alice", "umur": 30, "kota": "Jakarta"}
    for key in dictionary.keys():
        print(key,"-->", dictionary[key])

def no9():
    dictionary = {"nama": "Alice", "umur": 30, "kota": "Jakarta"}
    for value in dictionary.values():
        print(value)

def no10():
    banyak_siswa = {"kelas A": 25, "kelas B": 30, "kelas C": 28}
    for key, value in banyak_siswa.items():
        print(key,"-->", value)
    
def no11():
    dictionary = {"nama": "Alice", "umur": 30, "kota": "Jakarta"}
    dictionary.update({"pekerjaan": "Programmer"})
    print(dictionary)  

def no12():
    dictionary = {"nama": "Alice", "umur": 30, "kota": "Jakarta"}
    dictionary.popitem()
    print(dictionary)

def no13():
    dictionary = {"nama": "Alice", "umur": 30, "kota": "Jakarta"}
    dictionary["nama"] = "Bob"
    print(dictionary)

    dictionary['kota'] = "Bandung"
    print(dictionary)

    del dictionary["umur"]
    print(dictionary)

def no14():
    kelas_informatika = {}

    while True:
        nama = input("Masukkan nama mahasiswa: ")
        if nama == "":
            break

        try:
            nilai = int(input("Masukkan nilai (0-10): "))
            if nilai not in range(0, 11):
                print("Nilai harus 0-10!")
                continue
        except:
            print("Input nilai harus angka!")
            continue

        if nama in kelas_informatika:
            kelas_informatika[nama] += (nilai,)
        else:
            kelas_informatika[nama] = (nilai,)

    for nama in sorted(kelas_informatika.keys()):
        total = sum(kelas_informatika[nama])
        jumlah = len(kelas_informatika[nama])
        print(nama, ":", total / jumlah)

def no15():
    kelas_informatika = {}

    while True:
        try:
            nama = input("Masukkan nama mahasiswa: ")
            if nama == "":
                break

            nilai = int(input("Masukkan nilai (0-10): "))
            if nilai not in range(0, 11):
                raise ValueError

        except ValueError:
            print("Nilai harus angka antara 0 sampai 10!")
            continue
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh user")
            break
        except Exception as e:
            print("Terjadi error lain:", e)
            continue

        if nama in kelas_informatika:
            kelas_informatika[nama] += (nilai,)
        else:
            kelas_informatika[nama] = (nilai,)

    for nama in sorted(kelas_informatika.keys()):
        total = sum(kelas_informatika[nama])
        jumlah = len(kelas_informatika[nama])
        print(nama, ":", total / jumlah)
