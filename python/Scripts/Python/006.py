parsecs_input = input("Input number of parsecs : ") # pedimos al usuario el numero de parsecs
parsecs = int(parsecs_input)  #convertimos el str a int para poder hacer operaciones matematicas
lightyears = parsecs * 3.26156  # multiplicamos los parsecs
print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears") # introducimos el str de parsec dados por el usuario y convertimos los lightyears a str para poder imprimir toda la cadena