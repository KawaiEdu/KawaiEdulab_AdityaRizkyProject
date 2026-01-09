def hitung_maju(mn):
    if mn == 0:            
        print("done!, ")
        return
    print(mn)
    hitung_maju(mn+1)    

while True :
    Nm = int(input("tulislah angka untuk di hitung (rekomen 10 - 100), tulis ''10'' untuk keluar: "))
    if Nm == 0 :
        break
    else :
        hitung_maju(Nm)