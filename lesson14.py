qazwsxedcrfvtgbyhnujmikolp = {
    "stooly" : "meja",
    "privyet" : "halo",
    "ubiraysya" : "keluar",
    "daerug" : "teman",
    "tam" : "di sana",
    "kto ty" : "siapa kamu",
    "nye" : "Tidak",
    "da" : "iya",
    "moy" : "miliku"
}

#key = tuple(zip(*qazwsxedcrfvtgbyhnujmikolp))[0]
#key, value = zip(*qazwsxedcrfvtgbyhnujmikolp)
while True :
    print("berikut list kamus rusia sehari hari \n ////////////////bahasa rusia/////////////////////")
    print("\033[32m ", qazwsxedcrfvtgbyhnujmikolp.keys() ," \033[0m\n /////////////////////////////////////")
    print("pilih menu 0, lihat semua kamus 1, check arti 2, tambah kamus 3, hapus kamus")
    print("ketik Qrt untuk keluar program")
    
    jm = (input("pilih nomor (0,1,2,3) "))
    if jm == "0" :
       print("\033[32m ", qazwsxedcrfvtgbyhnujmikolp , "\033[0m ")
    elif jm == "1" :
        nm = input("pilih kata untuk menerjemahkan : ")
        if nm in qazwsxedcrfvtgbyhnujmikolp :
          print("\033[32m --/////arti///// \033[0m ", nm," = " , qazwsxedcrfvtgbyhnujmikolp[nm] , "\033[32m /////arti/////-- \033[0m")

    elif jm == "2" : 
       km = input("masukan kamus ")
       km2 = input("masukan arti kamus")
       qazwsxedcrfvtgbyhnujmikolp[km] = [km2]

    elif jm == "3" :
       kj = input("masukan kamus : ")
       if kj in qazwsxedcrfvtgbyhnujmikolp :
          del qazwsxedcrfvtgbyhnujmikolp [kj]

    elif jm == "qrt" :
       break

    else :
       print("pilihan tydack ada di daftra")