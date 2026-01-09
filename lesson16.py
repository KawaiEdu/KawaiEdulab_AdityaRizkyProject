buah1 = {"duren","apple","p'ear","jambu","cocofanto elefanto"}
buah2 = {"carot","duren","avocada","cocofanto elefanto","strawberry elephant"}

while True :
    print("abarayshya")
    print("pilih menu \n | 1,mencari kesamaan \n | 2,menggabungkan set \n | 3,lihat perbedaan \n | 4,keluar dari program")
    Ino1 = input("pilih 1 - 5 : ")
    if Ino1 == "1" :
        BYS = buah1.intersection(buah2)
        print("buah yang sama ( ada di kedua list ) " , BYS )

    elif Ino1 == "2" :
        G2V = buah1.union(buah2)
        print("menggabungkan 2 set ")
        print(G2V)

    elif Ino1 == "3" :
        pBdB = buah1.difference(buah2)
        print("buah yang kurang ( berbeda ) : " , pBdB )

    elif Ino1 == "4" :
        print("keluardari program")
        break

    else :
        print("wrong words looser")

        