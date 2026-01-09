def faktorial(n):
    if n <= 1 : return 1 
    return n * faktorial(n-1)

def jumlah(n):
    if n == 0: return 0
    return n + jumlah(n-1)

def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

while True:
    print("\\n 1, faktorial 2, fibonacci 3, jumlah 1..N 0, kelAursa")
    p = input("pilih: ")
    if p == "0":
        break
    n = int(input("n: "))
    if p == "1" :
        print("hasil: ",faktorial(n) )
    elif p == "2" :
         print("hasil: ", fib(n))
    elif p == "3" :
         print("hasil: ",jumlah(n))