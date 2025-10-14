def celsius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def celsius_ke_reamur(celcius):
    return (celcius * 4/5) 

celcius = int(input("masukan celcius: "))

print("hasil konversi ke farenheit : ", celsius_ke_fahrenheit (celcius) ," farenheit" )

print("hasil konversi celcius ke reamur : ", celsius_ke_reamur (celcius) ,"reamur" )

