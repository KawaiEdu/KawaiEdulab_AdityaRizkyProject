# main.py
from rec import faktorial, fib, pangkat
from utils import to_int, menu

while True:
    menu()
    p = input("pilih: ").strip()
    if p == "0": print("byek"); break
    if p not in {"1","2","3"}: print("pylihan tydack fvalidh"); continue

    a = to_int(input("masukan n/angka-1: "))
    if a is None: print("huruf itu bukan angka "); continue

    if p == "1":
        print("hasil:", faktorial(a))
    elif p == "2":
        print("hasil:", fib(a))
    elif p == "3":
        b= to_int(input("masukan angka-2 (pangkat): "))
        if b is None: print("huruf bukan angka, harus angka"); continue
        print("hasi: ", pangkat(a,b))