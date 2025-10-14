while True : 
        print("list minuman \n 1. teh manis = 5000 \n 2. air putih = 3000 \n 3. kopi = 7000"  )
        print(" 4. end ")
        uang = int(input("masukan jumlah uang kamu "))

        lous = int(input("pilih minuman (1-3) "))

        if lous == 1 :
            if uang >=  5000 :
                print("kembalian : ", uang - 5000 ,"terimakasih ")
            else:
                print("uang tidak cukup")
    
        elif lous == 2 :
            if uang >= 3000 :
                print("kembalian : ", uang - 3000 ,"terimakasih ")
            else:
                print("uang tidak cukup")

        elif lous == 3 :
            if uang >= 7000 :
                print("kembalian : ", uang - 7000 ,"terimakasih ")
            else:
                print("uang tidak cukup")

        elif lous == 4 :
            print("keluar dari program ")
            break

        else :
            print("pilihan tydack valid ")