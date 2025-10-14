suh = int(input("masukan suhu (°C) : "))
 
if suh > 40 :
    print("sangat panas")
    print("saran : memakai topi dan payung jika perlu")

elif suh > 30 :
    print("panas")
    print("saran : memakai baju baju lengan panjang")

elif suh > 20 :
    print("suhu normal")
    print("saran : memakai beju bebas")

elif suh >= 0 :
    print("dingin")
    print("saran : memakai baju tebal")

elif suh >= -50 :
    print("!titik beku!")
    print("saran : memakai baju sangat tebal dengan perlengkapan lebih")

else :
    print("di bawah titik beku normal")
    print("berbahaya : baju tebal 3x ")

print("\n")
print("^_^")