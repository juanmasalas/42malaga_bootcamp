import sys
if len(sys.argv) == 1:
    print("Uso : No se ha introducido ningún número. Necesitas dos números enteros")
    sys.exit
elif len(sys.argv) != 3:
    print("Error: Debes introducir dos números enteros.")
    sys.exit()
else:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except (ValueError, NameError):
        print("No se permiten letras ni numeros decimales")
        exit()
    print("Suma:\t\t", a+b)
    print("Diferencia:\t", a-b)
    print("Multiplicación:\t", a*b)
    try:
        print("Cociente:        ",    a/b)
    except ZeroDivisionError:
            print("Cociente:\t Error: División por cero")
    try:
        print("Resto:           ",   a%b)
    except ZeroDivisionError:
        print("Resto:\t\t Error: Modulo por zero")
    sys.exit()

           
