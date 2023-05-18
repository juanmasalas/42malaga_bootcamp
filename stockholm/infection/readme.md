README - Programa de cifrado de archivos Stockholm

Este es un programa de cifrado de archivos llamado Stockholm que puede cifrar los archivos con ciertas extensiones en una carpeta seleccionada. El programa también tiene una función para revertir la infección.

## Requerimientos

Este programa requiere Python 3.6 o superior y la biblioteca pycrypto. La biblioteca pycrypto se puede instalar ejecutando el siguiente comando:

```
pip install pycryptodome
```

## Uso

El programa Stockholm se puede ejecutar desde la línea de comandos. El siguiente es un resumen de las opciones de línea de comandos disponibles:

```
usage: programa_stockholm.py [-h] [-v] [-r clave] [-s]

Programa stockholm

optional arguments:
  -h, --help            muestra el mensaje de ayuda y sale
  -v, --version         muestra el número de versión y sale
  -r clave, --reverse clave
                        revierte la infección usando la clave especificada
  -s, --silent          no muestra output
```

### Cifrar archivos

Para cifrar los archivos en una carpeta, simplemente ejecute el programa sin argumentos adicionales:

```
python programa_stockholm.py
```

El programa buscará todos los archivos con ciertas extensiones en la carpeta ~/infection y los cifrará con una clave predefinida. Los archivos cifrados tendrán una extensión .ft agregada al final de su nombre de archivo original.

### Revertir la infección

Para revertir la infección, ejecute el programa con la opción -r y proporcione la clave de cifrado utilizada para cifrar los archivos:

```
python programa_stockholm.py -r mi_clave_ultra_seguraaaa
```

El programa buscará todos los archivos cifrados en la carpeta ~/infection y los descifrará utilizando la clave proporcionada. Los archivos descifrados tendrán su extensión .ft eliminada del final de su nombre de archivo original.

### Modo silencioso

Si no desea ver el output del programa, puede ejecutar el programa con la opción -s:

```
python programa_stockholm.py -s
```

## Advertencia

Este programa puede cifrar y descifrar archivos. Utilice este programa bajo su propio riesgo y asegúrese de hacer una copia de seguridad de sus archivos antes de usarlo.

Además, no utilice este programa para cifrar archivos que no le pertenecen. Es ilegal y puede resultar en consecuencias legales.