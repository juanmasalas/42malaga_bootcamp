import sys

# Comprobar si se proporciona exactamente un argumento y si es un número entero
if len(sys.argv) == 2 and sys.argv[1].isdigit():

    # Convertir el argumento a un número entero
    numero = int(sys.argv[1])

    # Comprobar si el número es impar, par o cero y mostrar el resultado correspondiente
    if numero == 0:
        print("El número es cero")
    elif numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
        
else:
    # Si no se proporciona exactamente un argumento o si el argumento no es un número entero, mostrar un mensaje de error
    print("Uso: python programa.py <número>")
    print("El argumento debe ser un número entero.")
    sys.exit()