x = float(input("angka y : "))
y = float(input("angka x : "))

tambah = lambda x,y: x + y 
kali = lambda x,y: x * y
kurang = lambda x,y: x - y
bagi = lambda x,y: x / y

pilihan = (input("pilih kalkualtor : \n tambah \n kali \n kurang \n bagi \n : "))

if pilihan == "tambah" :
    print(tambah(x,y))

elif pilihan == "kali" :
    print(kali(x,y))

elif pilihan == "kurang" :
    print(kurang(x,y))

elif pilihan == "bagi" :
    print(bagi(x,y)) 

else :
    print("pilihan tidak ada di daftar")