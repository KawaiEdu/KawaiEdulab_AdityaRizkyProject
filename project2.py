def tampilan_menu():
    print("semalat dantang ")
    print(" 1. tambahkan tujuan negara \n 2. tamplilkan tujuan negara \n 3. hapus tujuan negara \n 4. simpan ke file \n 5. muat daftar ke file \n 6. keluar dari program")

def tambah_negara(daftar):
    negara = input("masukan namka negra : ")
    daftar.append(negara)
    print("berhasil di tambahkan! ")

def tampilkan_daftar(daftar):
    if daftar:
        print("\n daftar negara : ")
        for i,negara in enumerate(daftar,start=1):
            print("{}.{}".format(i,negara))
    else:
        print("daftar negara tidak di temukn")

def hapus_negara(daftar):
    tampilkan_daftar(daftar)
    try:
        nomor=int(input("masukan nama negara yang ingin di hapus (angka): "))
        if 1 <= nomor <= len(daftar):
            negara= daftar.pop(nomor-1)
            print("{} berhasil di hapus dari tujuan negara.".format(negara))
        else:
            print("nomor negara tidak valid")
    except ValueError:
        print("input harus sebuah angka ")

def simpan_daftar(daftar):
    try:
        with open("daftar_tujuan_negara.txt", "w") as file :
            for negara in daftar:
                 file.write(negara + "\n")
                 print("daftar negara telah berhasil tersimpan ke file. ")
    except Exception as e:
        print("terjadi kesalaan saat menyimpan! : {}".format(e))

def muat_daftar():
    try:
        with open("daftar_tujuan_negara.txt", "r") as file :
            daftar = [line.strip() for line in file]
        print("daftar tugas berhasil di muat 💥")
        return daftar
    except IOError:
        print("💢terjadi kesalahan ->tidak ada file<-")
        return []
    except Exception as e:
        print("💢terjadi kesalahan saat memuat: {}".format_map(e))
        return
    
def main():
    daftar = muat_daftar()
    while True:
        tampilan_menu()
        pilihan = input("masukan pilihan (1-6): ")

        if pilihan == "1":
            tambah_negara(daftar)

        elif pilihan == "2":
            tampilkan_daftar(daftar)
        
        elif pilihan == "3":
            hapus_negara(daftar)
        
        elif pilihan == "4":
            simpan_daftar(daftar)

        elif pilihan == "5":
            daftar = muat_daftar()

        elif pilihan == "6":
            print("terimakasih ")
            break
        
        #elif pilihan == "7":
         #   print("anda telah menemukan easter egg \n ! ☆*: .｡. o(≧▽≦)o .｡.:*☆ ")

        elif pilihan == "7":
            print("TEXT BOOM TEXT BOOM TEXT BOOM TEXT BOOM \n TEXT BOOM TEXT BOOM TEXT BOOM TEXT BOOM TEXT \n BOOM TEXT BOOM TEXT BOOM TEXT BOOM TEXT \n BOOM TEXT BOOM TEXT BOOM TEXT BOOM  ")

        else :
            print("eror ->pilihan tidak ada di daftar<-")

main()