# Proyecto Arachnida

Arachnida es un proyecto que consta de dos scripts: Spider y Scorpion. Estos programas pueden ser scripts o binarios y cumplen con los siguientes requisitos:

## Spider

El programa Spider realiza web scraping de una página web con los siguientes requisitos:

- Permite extraer todas las imágenes de un sitio web de forma recursiva, proporcionando una URL como parámetro.
- Gestiona las siguientes opciones del programa:

```
./spider [-rlpS] URL
```

- Opción `-r`: descarga de forma recursiva las imágenes en la URL recibida como parámetro.
- Opción `-r -l [N]`: indica el nivel máximo de profundidad de la descarga recursiva. Si no se indica, se establecerá en 5.
- Opción `-p [PATH]`: indica la ruta donde se guardarán los archivos descargados. Si no se indica, se utilizará `./data/`.
- El programa descargará por defecto las siguientes extensiones de archivo: `.jpg/jpeg`, `.png`, `.gif` y `.bmp`.

## Scorpion

El programa Scorpion extrae los metadatos de los archivos de imagen, cumpliendo los siguientes requisitos:

- Recibe archivos de imagen como parámetros y es capaz de analizarlos en busca de datos EXIF y otros metadatos, mostrándolos en pantalla.
- El programa es compatible, al menos, con las mismas extensiones de archivo que gestiona Spider.
- Muestra atributos básicos como la fecha de creación, así como otros datos EXIF.
- El formato en el que se muestran los metadatos queda a elección del desarrollador.

```
./scorpion FILE1 [FILE2 ...]
```

Recuerda que en ambos programas debes desarrollar la lógica por ti mismo. No se permite utilizar funciones o librerías que realicen el trabajo principal, como wget o scrapy, ya que se consideraría trampa y resultaría en la suspensión del proyecto.

¡Disfruta del proyecto Arachnida y aprovecha la oportunidad para aprender sobre web scraping y manejo de metadatos en archivos de imagen!

