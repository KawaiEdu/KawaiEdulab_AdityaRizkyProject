def tulis_catatan():
    catatan = input("Masukkan catatan Anda: ")
    with open("catatan.txt", "a") as file:
        file.write(catatan + "\n")
    print("Catatan berhasil disimpan!")
