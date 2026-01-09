while True :
    print("\nMENU: [1] Sapa  [2] Hitung x 2  [0] Keluar")
    pilih = input("Pilih: ").strip()
    if not pilih :
        continue
    if pilih == "0":
        print("sampai jumphah ")
        break 
    elif pilih == "1" :
        Nama = input("insert name : ").strip()
        if not Nama:
            continue
        print("halo,", Nama + "!")
    elif pilih == "2":
        n = int(input("Masukan n: "))
        total = 0
        for i in range(1, n+1):
            total += i 
        print("jumlahj ", n , "=", total)
    else:
        print("OE OE back to one \n \n hello again 🙌👌")