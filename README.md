# proyecto-final
## **JUEGO DE DAMAS**

Para el proyecto final se lleva a cabo la creación de un juego de Damas que funciona a partir de la terminal de cualquier computador o sistema operativo que 
tenga preinstalado Python, como el lenguaje de programación fundamental que permite obtener o desarrollar una acción predeterminadas que se le solicite a dicha juego para que estas se ejecuten de manera satisfactoria.

### **¿por que un juego de damas?**

es un juego que aunque es bastante sencillo necesita una buena logica ya que como todos los juegos de mesa son de estrategia y un siempre un movimiento puede llevar a una derrota o a la victoria, y esto nos parecio bastante acorde con todo la tematica principal  del curso la cual es el desarrollo de logica ademas del desarrollo de agilidad mental.

<img width="387" alt="image" src="https://user-images.githubusercontent.com/109982186/192086029-bb75557f-e2d3-4780-a7c6-0fd8971dace2.png">

## Aplicaciones utilizadas

### **python**

Python es un lenguaje de programación orientado a objetos de alto nivel e fácil de interpretar con una sintaxis fácil de leer. Python, ideal para prototipos y tareas ad hoc, tiene un amplio uso en la informática científica, el desarrollo web y la automatización. Como lenguaje de programación para principiantes y con fines generales, Python admite muchos de los mejores científicos de computadoras y desarrolladores de aplicaciones a nivel global.

<img width="400" alt="img" src="https://blog.educacionit.com/wp-content/uploads/2020/02/paython-e1566991357500.png">

 ### **visual studio code**
 
 es un editor de código fuente desarrollado por Microsoft. Es software libre y multiplataforma, está disponible para Windows, GNU/Linux y macOS. VS Code tiene una buena integración con Git, cuenta con soporte para depuración de código, y dispone de un sinnúmero de extensiones, que básicamente te da la posibilidad de escribir y ejecutar código en cualquier lenguaje de programación.

<img width="400" alt="img" src="https://user-images.githubusercontent.com/49339/32078472-5053adea-baa7-11e7-9034-519002f12ac7.png"> 

     
## Librerías utilizadas  

### **Pygame:**

Pygame es un conjunto de módulos de Python diseñados para escribir videojuegos este añade funcionalidad a la excelente biblioteca de SDL. Esto le permite crear 
juegos con todas las funciones y programas multimedia en el lenguaje python.Ademas de ser altamente portátil y se ejecuta en casi todas las plataformas y sistemas operativos. 

Pygame es gratuita.ya que esta Lanzado bajo la licencia **LGPL**, puede crear juegos de código abierto, freeware, shareware y 
comerciales con él. 


<img width="578" alt="image" src="https://files.realpython.com/media/pygame-logo.e78e57db3000.png">

## Instalacion de pygame en sistemas operativos windows

La instalacion de pygame se hace por medio de la consola del computador , a la cual se accede por medio de windowa+R.

<img width="200" alt="image" src="https://rompetusilencio.net/images/blog/Open-the-Command-Prompt-in-Windows.jpg">

Esto abre un ventana en la parte inferior en la cual deveremos escribir las letras cmd, y esto abrira parte de la consola del dispositivo.

<img width="250" alt="image" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.groovypost.com%2Fwp-content%2Fuploads%2F2010%2F08%2Fimage_43.png&f=1&nofb=1&ipt=b90b200308e7d427f54dac15134bc7a981ddd4427286c51f06643b18e076ba62&ipo=images">

Ya aqui escribiremos lo siguiente pip install pygame y enter, esto comenzara la instalacion de pygame en el dispositivo.

<img width="479" alt="image" src="https://user-images.githubusercontent.com/109982186/192087043-12d9be38-0ef0-4ad7-86f2-567e4519a157.png">

## Contrucción del juego 

Para la construccion del juego se decidimos usar El paradigma de programacion orientada a objetos

y asi procedimos a identificar sus objetos y caracteristicas, entre ellos estan :

### **Constantes.py**

son todas aquellas variables que a lo largo del juego no cambiaran esta comprende cosas como:

🔴 La imagen de la corona en los reyes

⚪ El color del tablero y las fichas

🔴 El tamaño del tablero.

⚫ El numero de filas y columnas.

<img width="500" alt="image" src="https://i.imgur.com/zecfzjE.png">

### **Pieza.py**

Esta todos los metodos necesarios para la creaccion de la ficha:

✿ El que se dibuje.

✿ Su posicion dentro del cuadro.

✿ Calcular la posicion de cada ficha.

<img width="500" alt="image" src="https://i.imgur.com/xSXgwvl.png">

### **Juego.py**

Es el controlador de la clase tablero, ademas de contener:

◉ Todos los movimientos validos de cada ficha.

◉ Muestra circulo azul "(metodo(dibujar_movimiento_valido)"que indica movimientos validos disponibles.

◉ Permite el cambio de turno.

◉ percibe el cambio en la posicion de cada ficha.

<img width="500" alt="img" src="https://i.imgur.com/J0MqDyg.png">

### **Tablero.py**

La clase mas "importante" por asi decirlo es la clase tablero, la misma contiene:

☆ La creacion del tablero y diseño del tablero.

☆ El tablero que es una matriz de numeros que permiten que cada cuadrado tenga una posicion en x y con el Metodo(crear_tablero).

☆ El metodo(dibujar) que dibujas los cuadros.

<img width="500" alt="img" src="https://i.imgur.com/PEFuDPB.png">

## Glosario

### **Simple DirectMedia Layer**

es una biblioteca de desarrollo multiplataforma diseñada para proporcionar acceso de bajo nivel a audio, teclado, mouse, joystick y hardware de gráficos a través de OpenGL y Direct3D. Es utilizado por software de reproducción de video, emuladores y juegos populares, incluido el galardonado catálogo de Valve y muchos juegos de Humble Bundle. 

<img width="387" alt="image" src="https://briefedup.com/wp-content/uploads/SDL-SDL-Logo-768x532.png">

### **LGPL(Lesser General Public License)**

Es una licencia de derechos de autor ampliamente usada en el mundo del software libre y código abierto, lo que hace es permitir que los usuarios finales (personas, organizaciones, etc) tengan libertad de usar, estudiar, compartir (copiar) y modificar el software. Su objetivo es doble: recalcar que el software cubierto por esta licencia es libre y, por otro lado, protegerlo (mediante una práctica conocida como copyleft) de intentos de apropiación que restrinjan esas libertades a nuevos usuarios cada vez que la obra (software, plugin, template) es distribuida, modificada o mejorada. 

<img width="387" alt="image" src="https://fossa.com/blog/content/images/2021/08/LGPL.png">

### **OpenGL(Open Graphics Library)**

es una interfaz de programación de aplicaciones diseñado para representación 2D y 3D gráficos. Proporciona un conjunto común de comandos que se pueden usar para administrar gráficos en diferentes aplicaciones y en múltiples plataformas. 

Al usar OpenGL, un revelador puede usar el mismo código para representar gráficos en una Mac, PC o dispositivo móvil. Casi todo moderno sistemas operativos y los dispositivos de hardware son compatibles con OpenGL, por lo que es una opción fácil para el desarrollo de gráficos. Además, muchos tarjetas de video e integrado GPU están optimizados para OpenGL, lo que les permite procesar comandos OpenGL de manera más eficiente que otras bibliotecas de gráficos.

<img width="387" alt="img" src="https://www.patentlyapple.com/.a/6a0120a5580826970c0224df38fae1200b-800wi">

## Referencias

<a href="https://www.pygame.org/wiki/about">Acerca de - pygame wiki   

<a href="https://techlib.net/definition/opengl.html">Definicion OpenGL
 
<a href="http://www.libsdl.org/">Capa simple de DirectMedia  </a>
  
  
Realizado por : Karina Borja , Alejandro Parraga y laura holguin. - Estudiantes de Ingenieria de la Universidad Ean. 
<img width="20" alt="img" src="https://cdn-icons-png.flaticon.com/512/3861/3861923.png">

<img width="200" alt="img" src="https://universidadean.edu.co/sites/default/files/logo-horizontal-es.png">
