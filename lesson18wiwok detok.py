def kalkulator():
    try : 
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        operasi = input("masukan operasi (+,-,*,/)" )
        if operasi == "+" : 
            hasil = angka1 + angka2

        elif operasi == "-" :
            hasil = angka1 - angka2 
            
        elif operasi == "*" :
            hasil = angka1 * angka2

        elif operasi == "/" :
            hasil = angka1 / angka2
        
        else : 
            print("operasi tidak valid")
        return print(f"hasil : {hasil} ")
    except ValueError:
        print("input harus angka 😠 ")

while True :
    print("\n kalkulator sederhana ")
    kalkulator()
    agin = input("apakah anda ingin menghitung lagi? ya/tidak ")
    if agin.lower() != "ya" :
        print("terimakasih ")
        break