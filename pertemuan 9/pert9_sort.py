def no1():
    #bubble sort sederhana dgn user input
    my_list = []
    num = int(input("Masukkan panjang elemen list: "))

    for i in range(num):
        val = float(input(f"Masukkan elemen ke list: "))
        my_list.append(val)

    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    print("\nSorted : ")
    print(my_list)

def no2():
    #interaktif buble sort
    my_list = []
    swapped = True
    num = int(input("Masukkan panjang elemen list yang akan diurutkan: "))

    for i in range(num):
        val = float(input("Masukkan elemen list: "))
        my_list.append(val)

    while swapped:
        swapped = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                swapped = True
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    print("\nSorted:")
    print(my_list)

def no3():
    my_list = [8,10,6,2,4]
    my_list.sort()
    print(my_list)

def no4():
    #reverse sorting
    lst = [5, 3, 1, 2, 4]
    lst.reverse()
    print(lst)

def no5():
    list_1 = [1]
    list_2 = list_1
    list_1[0] = 2
    print(list_2)

def no6():
    #slice 1 awal:akhir
    my_list = [10, 8, 6, 4, 2]
    new_list = my_list [1:3]
    print(new_list)

def no7():
    my_list = [10, 5, 3, 8, 2]
    new_list = my_list[1:-1]
    print(new_list)

def no8():
    #slice 3 negatif:positif
    my_list = [10, 8, 6, 4, 2]
    new_list = my_list [-1:1]
    print(new_list)

def no9():
    my_list= [10, 5, 3, 8, 2]
    new_list = my_list[3:]
    print(new_list)

def no10():
    #slice 5 awal
    my_list = [10, 8, 6, 4, 2]
    new_list = my_list [3:]
    print(new_list)

def no11():
    my_list = [10, 8, 6, 4, 2]
    new_list = my_list[:]
    print(new_list)

def no12():
    my_list = [10, 8, 6, 4, 2]
    del my_list[1:3]
    print(my_list)

def no13():
    my_list = [1, 2, 3, 4, 5]
    del my_list[:]
    print(my_list)

def no14():
    my_list = [1, 2, 3, 4, 5]
    del my_list
    print(my_list)

def no15():
    my_list = [1, 3, 12, 4, 2]
    print(5 in my_list)
    print(12 in my_list)

def no16():
    my_list = [1, 3, 12, 4, 2]
    print(12 not in my_list)
    print(5 not in my_list)

def no17():
    my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
    largest = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]
    print(largest)

def no18():
    my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
    largest = my_list[0]

    for i in my_list:
        if i > largest:
            largest = i
    print(largest)

def no19():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    to_find = 5

    for i in range(len(my_list)):
        found = my_list[i] == to_find
        if found:
            break

def no20():
    lotre = [3, 7, 11, 42, 34, 49]
    angka_keluar = [5, 9, 11, 42, 3, 49]
    tebakan = 0

    for i in range(len(lotre)):
        if lotre[i] in angka_keluar:
            tebakan += 1
    print("Anda benar menebak sebanyak", tebakan, "angka.")

def no21():
    my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
    new_list = []

    for i in my_list:
        if i not in new_list:
            new_list.append(i)

    print(new_list)
