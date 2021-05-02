# Notas de Python



[TOC]



## CLASE 11/03/2021

Pycharm, editor/IDE de Python



python --version

Permite verificar la version de Python

## CLASE 18/03/2021

Ciclo de desarrollo de software

Requisitos, Analisis, Diseno, Codificacion y Pruebas



Los programas sencillos no requieren de muchas tecnicas, solo aquellos que son complejos



Buenas practicas

Programas mas elaborados se recomienda dividir el proyecto en fases, sprint o secciones



PEP 8, convenciones de codigo

De acuerdo a PEP 8, el maximo tamano de linea es de 79 caracteres



Zen of Python, guia para tomar decisiones

Evita repetir codigo



Refactoring, es la modificacion del codigo fuente sin cambiar su comportamiento. Es parte del mantenimiento del codigo que arregla errores y no anade funcionalidad.



Python permite hacer casos de prueba, que durante el testing permite saber si el codigo funciona con ciertos casos.



Para crear diagramas de flujo

Visual paradigm, luzy char



En Europa, muchos de los datos y software cientificos no tenian una estandarizacion. Surgio entonces la estandarizacion de los datos, que dio origen a los principios FAIR.



DOI, serie de caracteres unico que sirve como identificador.



### Python

Lenguaje interactivo, estructurado y de alto nivel

Caracteristicas del lenguaje:

Potente

Amigable

Intuitivo

Facil



Es un lenguaje interpretado que no requiere de compilacion.

Es un lenguaje de programacion multiparadigma (imperativo, funcional, orientado a objetos).



Versiones

Python 2 esta obsoleto, por lo que conviene Python 3

Algunas librerias ya no se actualizaron por haber sido reemplazadas por otras o por su bajo uso.

El codigo de Python 3 esta enfocado en Unicode en vez de ASCII como Python 2

En Python 3 las divisiones dan flotantes y en Python 2 enteros.



python --version

Permite conocer la version de python

which python

Permite conocer donde se encuentra python

pip, instalador de paqueterias de python



import sys

sys.version

print(sys.path)



Alt+Shift+E

Permite copiar una linea de codigo dentro de PyCharm y ejecutarla en la consola de Python



Shift+F6

Refactor

Permite cambiar el nombre de una variable dentro de un programa o varios archivos, incluyendo en comentarios.



Ctrl+F

Permite realizar una busqueda en el codigo, y pueden hacerse busquedas con expresiones regulares





## CLASE 08/04/2021

Pycharm

Crtl + D	Permite duplicar una linea de codigo

Alt+Shift+C	Muestra los cambios recientes en el programa



Se pueden visualizar los comentarios en la seccion TODO en la parte inferior



Anaconda, es parte dell ecosistema en Python

pyp install te permite installar librearias.



Anaconda permite tener ambientes donde se puede instalar varios programas sin afectar el otro ambiente.



Al instalar miniconda, instala paquetes basicos.

ANACONDA, incluye miniconda y paqueterias avanzadas, como bio python



BIOCONDA

Existen muchas herramientas que se han creado en bioinformatica y paqueterias.



Rosalind

Pagina que contiene ejercicios enfocados en Python y para bioinformatico, empezando desde 0

El apartado de Python esta enfocado de aprender lo basico de python



PYTHON como calculadora

Python permite hacer operaciones matematicas

Con **, puede usar potencias







**Strings**

Cadenas de caracteres

Var_name = "STRING"

Para un string, se usa ""

Para una palabra o caracter, se usa ''



Operadores de cadenasde caracteres

'+'	Permite concatenar strings

'-'

'*'	Permite multiplicar un string 

'/'

'=' 	Para asignar un string



Se pueden usar los operadores junto alsigno = para simplificar la expresion VAR = VAR 'OPERATOR' VAR

EJEMPLO

TEXTO = 'JOLO'

TEXTO = TEXTO + ' '		//O puede ser TEXTO += ' '



**METODOS**

Metodos, funciones que pertenecen a un objeto

Algunos son: len, find, replace



**LONGITUD**

Funcion len: 'len' permite medir la longitud de un string

len(var)



 **BUSCAR**

Para buscar dentro de un string la posicion de un(os) caracter(es), se usa la expresion VAR.find("STRING")

Ejemplo: print (mensaje.find("Hola"))	//Resultado sera la posicion del primer caracter dentro del string, siendo del 0 al n-1

**Python es case sentitive** 

Si no encuentra el resultado, la posicion dada sera -1



**MINUSCULAS/MAYUSCULAS**

Se pueden convertir un string a minusculas o mayusculas.

VAR.lower()

VAR.upper()



**REEMPLAZAR**

Se pueden reemplazar caracteres mediante replace

var.replace('original_character', 'new_character')

El new_character reemplazara al original_character



**CORTAR**

Se pueden cortar partes de un string o un caracter

var[first_char:last_char]

first_char es la posicion del primer caracter donde se cortara y se comenzara, y last_char la posicion en donde terminara, por lo que este caracter no se incluira.

Entonces, te permite obtener desde el primer caracter pero antes del ultimo caracter

Si se deja la posicion en blanco, cortara desde el inicio si es el primer caracter o el final si es el ultimo

var[:b]	var[a:]



var[position]

Corta solo el caracter en esa posicion



**Posiciones en un string**

Las posicion van del 0 a n-1, el ultimo caracter, siendo n la cantidad de caracteres

Tambien va de sentido contrario desdde el ultimo caracter hasta el primero, pero comenzando con el numero -1 hasta -n

0	  1	  2     3	 4

-5	-4	-3	-2	-1



**Secuencia de escape**

Para incluir caracteres especies, se usa \

\n

\t

\ ''	\\Deje un espacio porque no me deja junto



**Imprimir variables/funciones en string**

Iniciar el string con f y la variable, funcion, metodo dentro de corchetes {}

print(f'Texto a imprimir {Variable/function}')

print('string' + str(function(var)))

print('string', function/var)		\Al hacer esto, se inserta un espacio entre ambos



**Contar**

Contar caracteres en un string

var.count('pattern')

var = hello

var.count('l')

output: 2



**LECTURA Y ESCRITURA DE ARCHIVOS**

**Input**

input() Pasar un valor directo desde la terminal

open() Lee archivos de texto

Argumentos (-i = input, - o = output, --h = help)



print inserta un salto de linea al imprimir



Archivos binarios o comprimidos al estar en bytes, se abren de manera diferente



**open**

open("path/filename")

Pueden usarse rutas simbolicas/relativas o rutas absolutas



var.close()	  Cierra el archivo

var.readline		Lee una linea

var.read			  Lee el archivo

**Note:** You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

## Clase 22/04/2021

Errores que pueden ocurrir al abrir un archivo

El archivo puede no encontrarse o que tenga permisos especiales



**import** os

Importa una paqueteria. la cual tiene un metodo para obtener un directorio.

os.getcwd()	Obtiene la direccion actual

os.chdir("PATH")	Cambia de direcccion/ruta.



Working directory La ruta donde se esta trabajando

script path la ruta donde se ubica el script



Para leer un archivo, primero se tiene que abrir con open()



La funcion len toma el cuenta caracteres especiales, como salto de linea.



**rstrip**

Para eliminar caracteres del archivo, podemos usar la funcion rstrip

FILE.rstrip('characters')

The `rstrip()` method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.



Open es una funcion que posee parametros:

r	read	Abre y lee archivo o da error si no existe

a	append	Abre un archivo por apendice o crea archivo si no existe. La informacion se anadira al final del contenido.

w	write	Abre un archivo para escribir y crea uno si no existe

x	create	Crea archivo o regresa error si existe



Entonces esto habilita que podamos usar estos archivos despues con los metodos.

open("file", "parameter")

file.parameter("")



**Listas y loops**

List 	Estructura que almacena objetos como elementos.

list_name = ["element1", "element2", "element3"]

Los elementos de la lista pueden ser de diferente tipo de dato.



Para conocer el tipo de dato, existe la funcion type

type(var)



Para acceder a un elemento de la lista, se usa la posicion del elemento, siendo que las posiciones comienzan desde el elemento 0 al elemento n-1

list_name[index]

Tambien se puede usar rangos

list_name[first_element:last_element]

Tambien permite hacer saltos

list_name[first_element:last_element:tamanodelossaltos]

Esto tambien funciona con los strings



**Index**

Para buscar un elemento en la lista sin conocer el index, se utiliza el metodo index

list_name.index("value/string")



**Append**

Permite anadir elementos al final de la lista

list_name.append("value/string")



Las listas se pueden unir con el operador +

list3 = list1 + list2



La funcion len tambien permite medir el tamano de las listas



**Extend**

Metodo que permite extender una lista

list.extend(list2)



**Reverse**

Metodo que permite revertir los elementos de la lista

list.reverse()



Para imprimir el contenido de la lista, se usa str(list)



## Clase 29/04/2021

**Loops**

Operaciones repetitivas

for <var> in <iterable>:

​	<stament(s)>

Podemos usar una lista, un string (que es una lista), un archivo (donde se obtendria cada una de las lineas del archivo).



El for va recorriendo automaticamente en los valores de la lista

EJEMPLO:

```python
for character in "JOTARO":
    print(character)
```

output: 

J

O

T

A

R

O



**Indentaciones**

Python es sensible a las indentaciones



**split**

Cortar un string con split

var.split('character')

Permite cortar un string en base a un caracter.

Estos fragmentos se pueden guardar en una lista

list = var.split('character')



**readlines**

Metodo para leer todas las lineas, devolviendo una lista

var = file.readlines()

