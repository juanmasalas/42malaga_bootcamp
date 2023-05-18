import sys

# Comprobar si se proporcionan argumentos y unirlos en una única cadena
if len(sys.argv) > 1:
    texto = " ".join(sys.argv[1:])
    
    # Invertir el orden de los caracteres de la cadena y cambiar las letras mayúsculas por minúsculas y viceversa
    resultado = texto[::-1].swapcase()
    
    # Imprimir el resultado final
    print(resultado)
else:
    print("Uso: python programa.py texto")
    sys.exit()
