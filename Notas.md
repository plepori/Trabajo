#Importar templates de Boopstrap 

Cargar index en templates/blog
Crear carpeta static y 


#Manipulacion de base de datos
instanciar la clase: a pasa a contener todos los valores que tiene la clase familiar

    a = Familiar.objects.all() 

Una vez cargada la informacion, podemos manipular los datos de la siguiente manera

    a[0] muestra el primer objeto...
    a[0].nombre = "pablo" 
    a.save() 
    a[0].delete() #borrado

Agregar un familiar nuevo
python
    a = Familiar(nombre = "pablo", direccion = "calle 123") 
    a.save() 

Filtrar informacion por medio de identificadores

    a = Familiar.objects.filter(id=2)  # como filtrar datos de la base de datos, se utiliza por id
    a = Familiar.objects.get(id=3) # a se carga con el valor de objeto id 3

Carga de seed_data
    
    py manage.py shell < seed_data.py #terminal
    import seed_data # dentro del shell


- GIT:
1- git status: muestra los cambios que se hicieron en el codigo
2- git log: compara el local y remoto de git. (origin/main, origin/HEAD) en rojo muestra el git remoto, en celeste el local.
3- git add. -> git commit -m "mensaje"  -> git push origin main

history: muestra los comandos ejecutados

git checkout -b nuevarama # se crea nueva rama para trabajar en paralelo
git push origin nuevarma #pushea desde la nueva rama
dentro de la consola de github con merge pull request unimos las ramas main con la nueva rama

#Resolucion de problema al importar template startbootstrap
1- seguido al primer < head > escribir {% load static %}
2- reemplazar "css/styles.css" -> "{% static  'blog/css/styles.css' }"


Para crear en el Admin 
from django.contrib import admin
from prueba.models import Familiar


admin.site.register(Familiar)