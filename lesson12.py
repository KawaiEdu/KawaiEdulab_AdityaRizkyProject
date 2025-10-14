jdwlkgtanrndm = []
jdwlsklh = ["pelajaran" , "istirahat" , "pelajaran" , "pulANG" ]
krja = ["kerjakan tugas" , "istirahat" , "kerja" , "PULANG"]
wrkt = ["50 pushup" , "30 pull up" ," 50 situp" ]


while True :
    print("list : ", jdwlkgtanrndm )
    print("1 tambah kegiatan")
    print("2 hapus kegiatan")
    print("3 tambah kegiatan khusus ")
    print("4 KOPI kegiatan")
    print("5 tambah kegiatan di urutan tertentu ")
    print("6 keluar")
    pilihan = input("masukan pilihan ")

    if pilihan == "1" :
        kgtn = input("masukan kegiatan ")
        jdwlkgtanrndm.append(kgtn)

    elif pilihan == "2" : 
        kgtn = input("kegiatan yang mau di hapus : ")
        if kgtn in jdwlkgtanrndm :
            jdwlkgtanrndm.remove(kgtn)
        else :
            print("pilihan tidak ada di daftar \n")

    elif pilihan == "3" :
        kgtn = input(" pilih kegiatan (sekolah,kerja,workout) : ")
        if kgtn == "sekolah" :
            jdwlkgtanrndm.extend(jdwlsklh)

        elif kgtn == "kerja" :
            jdwlkgtanrndm.extend(krja)

        elif kgtn == "workout" : 
            jdwlkgtanrndm.extend(wrkt)

        else :
            print("tidak ada di daftar kegiatan khusus")

    elif pilihan == "4" :
        new_list = jdwlkgtanrndm.copy()
        print(new_list)

    elif pilihan == "5" :
        urtn = int(input("urutan ke : "))
        kgtn = input("masukan kegiatan ")
        jdwlkgtanrndm.insert(urtn , kgtn )

    elif pilihan == "6" :
        print("thankyou have a good day")
        break

    else :
        print("pilihan tidak tidak ada di daftar ")