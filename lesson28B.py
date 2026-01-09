def aman_bagi(a,b):
    try:
        return a/b
    except ZeroDivisionError :
        return "tidak bisa di bagi zero , 0 , nol"
    
print(aman_bagi(10,0))
