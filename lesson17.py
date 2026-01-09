def tulis_catatan():
    catatan = input("Masukkan catatan Anda: ")
    with open("catatan_adit.txt", "a") as file:
        file.write(catatan + "\n")
    print("Catatan berhasil disimpan!")
    file.close()

def baca_catatan():
    try : 
        with open("catatan_adit.txt", "r") as file:
            print("catatan harian anada : ")
            print(file.read())
            file.close()
    except FileNotFoundError :
        print("File Not Found")

while True :
    print("\nPilih menu:")
    print("1. baca catatan ")
    print("2. tulis catatan ")
    print("3. Keluar ")
    pilihan = input("masukan pilihan (1,2,3) ")

    if pilihan == "1" :
        tulis_catatan()

    elif pilihan == "2" :
        baca_catatan()
    
    elif pilihan == "3" :
        print("Terima kasih! Sampai jumpa.")
        break 

    else : 
        print("sybau")

    