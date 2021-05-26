# Notas de Python



[TOC]



## Clase 11/03/2021

Pycharm, editor/IDE de Python



python --version

Permite verificar la version de Python

## Clase 18/03/2021

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





## Clase 08/04/2021

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



## Clase 06/05/2021

Recomendacion: Comentarios en infinitivo, cortos y que estan arriba de la linea de codigo y no al lado



### Iteradores

Una variable puede ser iterable (numbers = [1,2,3])

Existen iteradores que son agentes que hacen realmente la iteracion sobre un iterable

iterador = iter(numbers)

iter() = Sirve para crear una variable iterador



next(). Funcion que solo funciona con iteradores, para acceder a los elementos de la lista. Recorre los elementos de una variable iterable, pero una vez acabado de ejecutar el codigo, guarda la posicion donde se quedo.



### Generadores 

Se crea un generador (objeto iterador) y se almacena en una lista.

Genera un objeto que guarda a una variable



lista= [operation for n in numbers]

lista= [n+4 for n in numbers]



Los generadores son iteradores, y se decide si guardarlos como listas o iteradores

Si se usa (), se crea un iterador y se puede acceder a los elementos resultantes del generador

lista= (n+4 for n in numbers)



### Enumerate

Puede dar el valor resultante y el contador

Es un iterador



se accede con list a la lista resultante del primer elemento.



Se puede avanzar con next a cada elemento

e = enumerate(numbers)



#### for con mas de una variable

Si en un for se usa enumerate, devuelve una lista, y por lo tanto podemos guardar cada valor en ciertas variables



for i, num in enumerate(numbers)



i guarda la posicion y enumerate guarda el numero.

(i, num)



### FUNCIONES

Para crear una funcion, se usa def

```python
def function():
	x = 2
    return x
```

Usa variables locales

def define la funcion.

return regresa un valor de la funcion



Primero se definen las funciones para despues llamarlas



Las variables pueden recibir argumentos

def function(var1)



Las funciones no guardan un valor, sino que realizan una operacion, y sus variables locales usarse fuera de la funcion



A partir de funciones se pueden crear paquetes para usar en otros codigos.



**Debug**

Pycharm tiene una funcion que permite correr hasta cierta linea, haciendo clic en la linea donde se desea parar.

Para obtener el resultado, se hace un Debug, que da el valor de todas las variables.

Se pueden tener multiples paros, y se puede ir siguiendo los valores de las variables



Redondear

Permite redondear un resultado

round(var, number_of_digits)



Las funcion al recibir argumentos pueden recibir variables y valores. Se puede poner como parametro su nombre asignandole el valor, o sea si se conoce el nombre de los parametros se puede dar un valor, y el orden de estos parametros no influye.

function(a="texto", b= 4)

function(b= 4, a="texto")

function(a, b)

function("texto", 4)



Si se comenzo nombrando los parametros, se espera que los siguientes esten nombrados, por lo que si los siguientes no lo estan entonces dara un error

function(a="texto", 2) ----> ERROR



Default

En los parametros, se puede tener un valor default en la funcion

def function(a, b = 2)

Al llamarse la funcion se puede cambiar el valor



Testing

Se puede checar que el codigo funciona con assert



assert es una funcion que permite igualar una variable/funcion a un valor que se espera, y ver si es verdarero.

Da un error de Assertion Error si no se cumple, y termina el codigo con 0 cuando se cumple (no hubo error)

assert suma(4, 5) == 9

TAREA: FUNCION QUE CALCULE EL PORCENTAJE DE UNA LISTA DE AMINOACIDOS. EL VALOR DEFAULT (PRIMER ELEMENTO) SERAN LOS AMINOACIDOS HIDROFILICOS

PIDE EL PORCENTAJE CONJUNTO DE LOS AMINOACIDOS SOLICITADOS



NOTA: LAS TAREAS EN PYTHON SERAN PARA MAS TARDAR ANTES DEL MIERCOLES



## Clase13/03/2021

Encapsulacion

Dividr el codigo en funciones, dividir un programa en piezas mas pequenas

Importar funciones

Se tiene que dar la ruta del archivo, y en ves de slashes se usan puntos.

data.file = data\file.py



from file import function

function()



import file as name

name.function()



Siguiente tema

Condicionales

True y False

Se da que una expresion es verdadera si al evaluarla se da el valor de 1, creoooo

True y False no son strings

== Evalua si dos variables tienen el mismo valor

<

!=

in Si un valor esta en una lista

is evalua si dos variables apuntan al mismo objeto

startswith(), isupper(), islower()



La sentencia if

if  condition:

​	code

permite evaluar una funcion si es verdadera

Sentencia else

else:

​	code

Permite ejecutar un codigo con la condicion evaluada por if es falsa

Sentencia elif

Permite evaluar una segunda condicion si una condicion anterior no se cumplio



if condition:

​	code

elif condition2:

​	code



Si te tienen muchas setencias, lo que provoca es que aumente el nivel de indentacion, por lo que no es preferible tener muchas sentencian anidadas



if

​	if

​	else

​		if

​			if

Tambien los else se pueden cambiar por elif, en este caso.

if

​	if

​	elif

​	else

ra

Libreria random

Permite obtener secuencias aleatorias

random.choice Devuelve un elemento aleatorio de una secuencia



While

Permite repetir un codigo mientras se cumpla una condicion



Condiciones complejas

and evalua si dos condiciones se cumple

or evalua si una de las dos condiciones se cumple



Mediante parentesis, (), se establece la jerarquia de las condiciones, indicando cuales se hacen primero



Not

Permite cambiar el valor de una condicion (Verdadero a falso y falso a verdadero)



Nota: al hacer un return en un funcion, el retornar una condicion devuelve verdadero o falso

return 5>5 

El ejemplo devuelve falso



Archivo .csv

Archivo separado por comas



Tarea Drosophila

Para la tarea hacer un solo programa, y no un programa para cada caso. Todo se imprimira a la vez



## Clase 20/05/2021

### Manejo de errores y argumentos

syntax errors: Mala indentacion o falta de sintaxis

typos: Errores en el nombre de variables/funciones

bugs: Errores que tienen que ver con como el programador comprendio el problema, funciona pero no es lo que se busca



IOError: [Errno 2] No such file or directory: 'missing.txt'  



exception handling o manejo de errores



### Try y except

try y except funcionan como for /if



### Error as variable

Los errores se pueden guardar como variables

ex.args[0] permite acceder a los errores

ex.strerror



import os

os.remove remueve archivo



### Uso de else

try

except

else



### finally

Permite ejecutar codigo sin importar si hubo excepciones

```python
try:

	code

except ExceptionType1:

	code

except ExceptionType2

	code

finally

	code
```



### try anidado

Los try pueden ser anidados

```python
try:
	f = open('data/7-file_num.txt')
	try:
		my_number = int(f.read())
	except ValueError:
		print('not an integer!')
	finally:
		f.close()
		print("the file was closed")
except IOError:
	print('cannot open file')  
```



### Raise

raise permite generar un error en el codigo



```python
e = ValueError("Description")

raise e
```

Otra sintaxis mas comun

```python
raise ValueError("Description")

```



### Clase para errores especiales

class AmbiguousBaseError(Exception):
	pass  



Argumentos

