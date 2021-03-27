# Notas de markdown

Con simbolo de gato, creamos un titulo.

Existen niveles de titulos.

# H1 #
## H2 ##
### H3 ###
#### H4 ####
##### H5 #####
###### H6 ######

## Funciones basicas

### Enfasis

Si se quiere enfantizar, se utilizan asteriscos o guiones bajo entre la palabra de interes.

Para las italicas se requiere solo uno en cada lado; para negritas se requieren dos en cada lado; para 'rayar' la palabra se usa ~~ ~~.

_dado_ 

**sopa**

~~Lolito~~

Se pueden combinar todos los estilos.

***~~Lolo~~***



Algunos editores pudieran no tener ciertas funciones, por lo que siempre se debe usar las funciones estandar para evitar problemas o para verificar como son en el editor.



### Listas

Para crear listas, se pueden usar puntos, asteriscos, signos menos o mas.



### Links

La sintaxis para crear un link es '[](URL)', siendo lo que este entre [] el texto que llevara a la liga.

Se puede anadir un titulo cuando el puntero se coloca sobre el link al agregar entre comillas el titulo despues del URL dentro de los parentesis (URL "").

 ...

Se puede hacer una referencia a un repositorio, en caso de tener una pagina en un proyecto web, se pueden acceder a otros archivos.

...

En algunos editores no reconoce ligas si solo se pega el URL.

[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com



### Imagenes

Se pueden insertar imagenes con la estructura de ! [ alt text ] ( URL ), sin los espacios

<img src="https://i1.sndcdn.com/avatars-QOlRqyVHuGqcMDtS-puSyXg-t500x500.jpg" alt="alt text" style="zoom:33%;" />

alt text, es el metadata de la imagen, sirve para describir la imagen



Para ver la lista de archivos/directorios de mi actual directorio de trabajo uso `ls` y para saber cual es mi directorio de trabajo es el comando `pwd`

Para resaltar una linea, se utilizan los caracteres ``

Para resaltar un codigo, se utilizan tres ```, uno al inicio y otro al final.

En algunos editores se puede indicar el lenguaje, al usar ``` LENGUAJE 

Al indicar el lenguaje, se resalta la sintaxis



```perl
print "HOLA"

```



```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```



```python
s = "Python syntax highlighting"
print s
```



```
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
```



Los documentos creados pueden ser convertidos en otros formatos



R markdown permite interpretar y convertir documentos a ciertos formatos.



### Tablas

Se pueden crear tablas

Los puntos indican como alinear el texto, :

| Tables             |   Are    |  Cool |
| ------------------ | :------: | ----: |
| columna 3 alineada | derecha  | $1600 |
| columna 2 alineada | centrada |   $12 |
| zebra stripes      | are neat |    $1 |