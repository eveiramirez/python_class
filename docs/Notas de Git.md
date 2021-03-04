# Notas de Git

## CLASE 25/02/2021

Mostrar la configuracion de git

$ git config --list



Cambiar globalmente el nombre de usuario

$ git config --global user.name "Nombre"



Cambiar globalmente el correo del usuario

$ git config --global user.mail "user@gmail.com"



Inicializar git en un directorio

$ git init



Obtener el estatus de git

$ git status



Crear un area de inicio que guardara los cambios del archivo, controlando el archivo

$ git add $FILE



Guardar la version del archivo final en el repositorio

$ git commit -m "Indicar que se hizo"

-m Mensaje corto, como 70 caracteres

-a Mensaje largo, crear un asunto y cuerpo

## CLASE 04/03/2021

El directorio se puede mover a otras rutas/carpetas.

$ git commit --amend -m "Mensaje"

Modificar el mensaje anterior



Si se quisieran hacer modificaciones a posterior del commit, puede haber problemas



$git diff

Mostrar las modificaciones de lo actual con el area de preparacion

--staged Compara el staging area con el repositorio



$nano

Editor de texto bash



$git log

Muestra en orden cronologico inverso los commits realizados

-N Indica el numero de commit que se quieren obtener

--oneline Identificar reducido de 7 caracteres con el commit, resumido

