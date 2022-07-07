from concurrent.futures.process import _chain_from_iterable_of_lists
from django.db import models

# Create your models here.
# Un modelo en django es basicamente crear una clase
# Atraves de un ORM(Object Relational Mapping)
# Es un componente que tiene django para poder
# Interactuar con una base de datos mediante 
# el uso de POO, es decir un OBJETO 
# en este caso nuestro modelo es "Curso"

# Esta clase se va a migrar como una tabla dentro 
# de nuestra base de datos

class Curso(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    creditos=models.PositiveSmallIntegerField()

    # __str__ es un metodo dentro de las clases que
    # permite imprimir un determinado texto cuando
    # hagamos la impresion de un objeto
    # en este caso vamos a imprimir el nombre del curso y sus creditos
    def __str__(self):
        texto="{0} - ({1}) CREDITOS"
        return texto.format(self.nombre, self.creditos)
