from django.http import HttpResponse
import datetime
from django.template import Template, Context
#Siempre deben retornar el httpResponse y deben resibir como parámetro el request

class Persona(object):
    def __init__(self, nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
        


def saludo(request):  #Primera Vista o view
    '''
    -En esta función primero abrimos el documento, con el método open y lo guardamos en una variable. Luego creamos el template metodo, que recibe 
    como parámetro el documento anteriormente abierto y lo lee con la funcion read(). Luego cerramos el documento para que no siga consumiendo
    
    recursos.
    -Luego creamos el contexto(es obligatorio), el que recibe como parámetro variables, funciones etc. En este caso recibe un diccionario
    el cual vamos a utilizar para mostrar sus valores en la página web. 
    
    -Luego reenderizamos el documento pasándole cómo parámetro, el contexto. Para que las variables puedan ser visibles cuando sean utilizadas
    en el documento web.
    
    -En el contexto podemos ver que, se pueden agregar además de diccionarios, listas también y poder mostrarlas en el documento web
    '''
    
    p1=Persona("Sergio Santiago","Herrera Gauna")
    
    fecha_actual = datetime.datetime.now()
    
    temas_delcurso=[]
    
    doc_externo=open("C:/Users/Santi/Desktop/Repositorios Clonados/Curso-Django/Proyectos Django/Proyecto1/Proyecto1/Plantillas/miplantilla.html")
    
    plt=Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"fecha":fecha_actual, "temas":temas_delcurso})
    
    documento=plt.render(ctx)
    
    return HttpResponse(documento)

def despedida(request): #Segunda Vista o viewmi
    return HttpResponse("Hasta Luego Alumnos de Django")

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    texto = '''
    <html>
    <body>
    <h1> Fecha y hora actuales %s</h1>
    </body>
    </html>
    ''' % fecha_actual
    return HttpResponse(texto)

def calculaEdad(request, edad,agno):
    periodo=agno-2019
    edadFutura=edad+periodo
    documento = "<html><body><h2> En el año %s tendrás %s años" %(agno,edadFutura)
    
    return HttpResponse(documento)