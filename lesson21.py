import time

def spam_bapak_teman() :
    bapak_teman = ["siswanto","yanto","budi","roma","yohanes","wasis","anang","dedi","miftah","johoni","tersigma potter"]
    for item in bapak_teman :
        print("ada bapak", item)
        time.sleep(1)
    
def mana() :
    HR = input("ketik 1 untuk mul'ay ")
    if HR == "1" :
        spam_bapak_teman()
    elif HR == "2" :
        for i in range(50) :
            print("101001101010010110010101001001010101010010101101001")
            time.sleep(0.05)
            print("100101010101010100101110101001010100101011010101010")
            time.sleep(0.05)
            print("100100101101001010110101001010101010100110101001010")
            time.sleep(0.05)
    
    elif HR == "3":
        print("halah")
        time.sleep(1)
        quit

    else :
        print("ojok ngawur lho")

while True :
    mana()