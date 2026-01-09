def discon_hraga(harga,persen):
    potongan = harga * persen / 100
    return harga-potongan
print(discon_hraga(10000, 50))

def halo(nama='Siswa'):
    if nama == 'siswa' :
        print("halo , user1class 'S' ")
    else :
        print(f"halo{nama}")
halo("kAk AqIl")
halo("kAk NeIsHyA")
halo()
halo("susilo budi prabowo")

def perkalian(a, b=2):
    return a * b
print(perkalian(4)) 
print(perkalian(4, 5))