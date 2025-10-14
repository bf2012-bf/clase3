s = 0

def c_f(c):
   return 9/5 * c + 32

def f_c(f):
    return (f - 32) * 5/9

while s < 3:
    print("Seleccione la operación:")
    print("1. Celcius a Farenheit")
    print("2. Farenheit a Celcius")
    s = int(input())
    while s > 2 or s < 1:
        print("Error! Operación no existe, ingrese una opción correcta:")
        s = int(input())
    if s == 1:
        print("Escriba el valor de temperatura en °C:")
        v = float(input())
        print(c_f(v),"°F")
    else:
        print("Escriba el valor de temperatura en °F:")
        v = float(input())
        print(f_c(v),"°C")      