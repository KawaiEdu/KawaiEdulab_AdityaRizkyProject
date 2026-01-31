class hewan :
    def __init__(self,nama,jenis,suara):
        self.nama = nama
        self.jenis = jenis
        self.suara = suara

    def bergerak(self):
        return f"{self.nama} sedang bergerak "
    
    def bersuara(self):
         return f" {self.nama} suara : {self.suara}"
    
class manusia :
        def __init__(self,nama,umur,pekerjaan):
            self.nama = nama
            self.umur = umur
            self.pekerjaan = pekerjaan 

        def perkenalan(self):
            return f"halo nama saya {self.nama}, umur {self.umur} tahun ,bekerja sebagai {self.pekerjaan}" 
        
        def pekerjaan(self):
            return f" {self.nama} sedang bekerja sebagai {self.pekerjaan}"
        
class benda:
        def __init__(self,nama,fungsi,bahan):
            self.nama = nama
            self.fungsi = fungsi
            self.bahan = bahan

        def deskripsi(self):
            return f"{self.nama} terbuat dari {self.bahan} guna for {self.fungsi}"
        

def main():
     kucing = hewan("gattito","kocheng","meong")
     anjing = hewan("duggo","anjing","ISHOW SPEED")
     kakacil = manusia("aqel","22.22","tutor")
     pakwowo = manusia("wowok","77","presiden / raja sawit")
     tripod = benda("tripod", "vlogging / stand hp", "besi / plastic ")
     hp = benda("handphone","social/daily/work","ironmen")
     brick = benda("batu bata", "build / bangunan", "batu cik")

     while True:
          print("\n menu program")
          print("1,tampil aktifitas hewan")
          print("2, aktivitas human")
          print("3, tampil akitivtas benda")
          print("4, keluar")
     
          pilihan = input("pilih 1-4 ")
     
          if pilihan == "1" :
               print(kucing.bergerak())
               print(kucing.bersuara())
               print(anjing.bergerak())
               print(anjing.bersuara())

          elif pilihan == "2":
               print(kakacil.perkenalan())
               print(kakacil.pekerjaan())
               print(pakwowo.perkenalan())
               print(pakwowo.pekerjaan())

          elif pilihan == "3":
               print(tripod.deskripsi())
               print(hp.deskripsi())
               print(brick.deskripsi())
               
          elif pilihan == "4":
               print("ty kel")
               break
          
          else :
               print("try again")

if __name__ == "__main__":
     main()