# Notas de Git

## CLASE 25/02/2021

Mostrar la configuracion de git

$ git config --list



Cambiar globalmente el nombre de usuario

$ git config --global user.name "Nombre"



Cambiar globalmente el correo del usuario

$ git config --global user.mail "user@email.com"



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

HEAD~# Permite comparar con las cabeceras. # es el numero



$nano

Editor de texto bash



$git log

Muestra en orden cronologico inverso los commits realizados, con el identificar, autor, fecha y el commit

-N Indica el numero de commit que se quieren obtener

--oneline Identificar reducido de 7 caracteres con el commit, resumido

--author="" Permite indicar el autor



$git status

-u



$git show 

Muestra mas detallado el commit realizado

HEAD Permite indicar la encabecera



$git checkout

Permite recuperar versiones anteriores



$git rebase --interactive [IdCommit]^

Modifica el commit, y cambia los identificadores



## CLASE 11/03/2021

.gitignore

Se establecen las reglas que ignoraran los archivos especificados.



git add -f

Permite ignorar el .gitignore



git status 

--ignored

Permite ver los archivos ignorados

-u

Permite ver las carpetas ignoradas



!<FILE>

Permite ignorar el archivo o lo indicado, negandolo



### GITHUB

git remote add origin <URL>

Permite indicar el repositorio con el que se comunicara



git remote -v

Permite identificar el repositorio comunicado



git push origin master

Subir lo que vive en la rama master al repositorio remoto

Carpetas vacias no aparecen en el repositorio remoto, por no haber archivos que controlar



git pull origin master

Bajar el contenido del repositorio remoto 



OpenScience



README, archivo que explica el proyecto