def discon(harga, persen):
    potongan = harga * persen /100
    return harga - potongan

def pajak(harga, persen):
    hitung_tambahan = harga * persen / 100
    hitung_hasil = harga + hitung_tambahan
    return hitung_hasil

while True:
    print("/n1. diskon","2.pajak 3.keluar")
    chiez = int(input("masukan pilihanmu"))

    if chiez == 1:
        harga = int(input("masukan maharaga: "))
        persen = int(input("masukan persen"))
        hasil_discon = discon(harga, persen)
        print(f"diskon afalah {hasil_discon}")
    elif chiez == 1:
        harga = int(input("masukan harga: "))
        persen = int(input("masukan persen: "))
        hasil_pajak = pajak(harga, persen)
        print(f"pajak adalah {hasil_pajak}")
    elif chiez == 3 :
        print("fine shankyou gedbwye 🙌 ")
        break
    else :
        print("1001010101001010010101001001101010101")
        print("1010010110101010010101010100101010101")
        print("1001010101001010010101001001101010101")
        print("1010010110101010010101010100101010101")
        print("1001010101001010010101001001101010101")
        print("1010010110101010010101010100101010101")
        print("1001010101001010010101001001101010101")
        print("1010010110101010010101010100101010101")
        print("1001010101 ' salah oi ' 1110101010101")
        print("1010010110101010010101010100101010101")
        print("1001010101001010010101001001101010101")
        print("1010010110101010010101010100101010101")
        print("1001010101001010010101001001101010101")
        print("1010010110101010010101010100101010101")
        print("1001010101001010010101001001101010101")
        print("1010010110101010010101010100101010101")
        print("1001010101001010010101001001101010101")
        print("1010010110101010010101010100101010101")