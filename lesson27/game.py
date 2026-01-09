# game.py
import random
from utils import valid_int
target = random.randint(1,20)
while True :
    raw = input("tebak 1..20; ")
    n = valid_int(raw)
    if n is None :
        print("maukan angka bykan hyuruf abcgdsjedkehaidjklmneionp ?! ") ; continue
    if n == target : print("benar!"); break
    print("terlalu","kecil" if n < target else "besarR")