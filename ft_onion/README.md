
# Project Title

A brief description of what this project does and who it's for

# Proyecto ft_onion

El proyecto ft_onion tiene como objetivo crear una página web y hacerla accesible desde la red Tor mediante la creación de un hidden service. Un hidden service es un servicio web que se oculta en la red Tor.

## ¿Qué es la red Tor?

La red Tor es una red anónima y descentralizada que permite a los usuarios navegar por Internet de forma anónima. Utiliza una serie de nodos encriptados para enmascarar la identidad y la ubicación del usuario, proporcionando privacidad y anonimato en línea.

## Características del proyecto

- El servicio web consistirá en una página web estática, representada por un solo archivo `index.html`. El contenido de la página es de libre elección.
- Se utilizará Nginx para configurar el servidor web. No se permiten otros servidores o frameworks.
- La página web será accesible a través de una URL del tipo `xxxxxxxxx.onion`, donde `xxxxxxxxx` será una identificación única generada para el hidden service.
- El acceso a la página web se realizará mediante HTTP en el puerto 80.
- El acceso al servidor se habilitará por SSH en el puerto 4242.
- No se deberá abrir ningún puerto adicional ni establecer reglas de firewall.

## Parte Bonus

La evaluación de los bonus se llevará a cabo SOLAMENTE si la parte obligatoria del proyecto es PERFECTA. En caso contrario, los bonus serán ignorados.

Puedes mejorar tu proyecto con las siguientes características adicionales:

- Fortificación de SSH: Se evaluará detenidamente durante la evaluación. Debes implementar medidas de seguridad adicionales para fortalecer el acceso por SSH.
- Creación de una web interactiva: Puedes desarrollar una página web más impresionante y con mayor interactividad que una simple página estática. Puedes utilizar librerías externas para lograrlo, pero no se permite el uso de frameworks. Si no comprendes la diferencia entre una librería y un framework, es mejor evitar su uso.

¡Aprovecha al máximo este proyecto ft_onion y sumérgete en el mundo de la creación de servicios web en la red Tor!