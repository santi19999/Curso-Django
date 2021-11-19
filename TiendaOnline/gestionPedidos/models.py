from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(blank=True, null=True)#Le indicamos a django que el campo no es requerido y puede quedar vacío
    tel=models.CharField(max_length=7)

class Articulos(models.Model):
    nombre=models.CharField(max_length=50)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()
    
    def __str__(self): #Para poder mostrar los datos de la base de datos ya que los retorna como objetos query
        return 'El nombre es %s, la sección es %s y el precio es %s' % (self.nombre,self.seccion,self.precio)
    
    
class Pedidos(models.Model):
    
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
    
    
