from django.http import HttpResponse
import datetime
from django.template import Template, Context
#Siempre deben retornar el httpResponse y deben resibir como parámetro el request


def saludo(request):  #Primera Vista o view
    doc_externo=open("C:/Users/Santi/Desktop/Repositorios Clonados/Curso-Django/Proyectos Django/Proyecto1/Proyecto1/Plantillas/miplantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
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