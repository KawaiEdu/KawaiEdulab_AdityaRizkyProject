dafter_belanja = []

while True :
    print("\n daftar belanja : ", dafter_belanja )
    print("tambah")
    print("hapus")
    print("keluar")
    pilihan = input("pilih opsi : ")

    if pilihan == "tambah" :
        item = input("pilihan masukan item ")
        sorts = int(input("di urutan ke? "))
        dafter_belanja.insert(sorts,item)

    elif pilihan == "hapus" :
        item = input("hapus item: ")
        if item in dafter_belanja :
            dafter_belanja.remove(item)
        else :
            print("item tidak ada di daftar")

    elif pilihan == "keluar" :
        print("keluar dari program")
        break

    else :
        print("\n !!!pilihan tidak valid!!!")

