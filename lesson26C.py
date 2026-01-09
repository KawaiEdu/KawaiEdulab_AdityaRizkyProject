import sys
import time
from functools import lru_cache

def menu():
    print("\n =========== piring 10 gram Antinigbass (-rekursivehhhhhh-)")

    print("1.rekursifma nroremalll (FYboNaCy)")
    print("2.deep rekursif (- neshted lisrt shumm)")
    print("3.memoization (fYbOnAcY omptimizzhed)")
    print("4.keluar")
    chochiche = input("mau pyliph yangh manahhhkkhkk 1,!.2,@.3,$.4,%.")
    return chochiche

def fibbonaci_rekursif(n):
    if n<= 1 :
        return n
    return fibbonaci_rekursif(n-1)+fibbonaci_rekursif(n-2)

def deep_sum(data):
    total = 0
    for item in data:
        if isinstance(item, list):
            total += deep_sum(item)
        else:
            total += item
            return total
        
@lru_cache(maxsize=None)
def fibbonaci_memoization(n):
    if n <= 1:
        return n
    return fibbonaci_memoization(n-1) + fibbonaci_memoization(n-2)

def main():
    while True:
        chochiez = menu()
        if chochiez == '1':
            n = int(input("masukan nilay fybonACI:"))
            start = time.time()
            result = fibbonaci_rekursif(n)
            end = time.time()
            print(f"hasil:{result}(waktu:{end-start:4f}detik)")
        elif chochiez == '2':
            nested = eval(input("masukan list bersarahng contoh : \n 1,2,3,4,5:"))
            result = deep_sum(nested)
            print(f"total penjumlahan:{result}")
        elif chochiez == '3':
            n = int(input("masukan nilai n untuk fybonACI(memoization:"))
            start = time.time()
            result = fibbonaci_memoization(n)
            end = time.time()
            print(f"hasil:{result}(waktu:{end-start:4f}detik)")
        elif chochiez == '4':
            print('fine shank you')
            sys.exit()

        elif chochiez == '':
            print()
        else:
            print("oi oi (111111111111001010000000100010101001010101010010101000010101110110)")

if __name__=="__main__":
    main()