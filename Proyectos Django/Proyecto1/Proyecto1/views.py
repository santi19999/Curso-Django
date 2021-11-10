from django.http import HttpResponse
import datetime
#Siempre deben retornar el httpResponse y deben resibir como parámetro el request


def saludo(request):  #Primera Vista o view
    texto = '''
    <html>
    <body>
    <h1> Hola alumnos esta es nuestra primera página con Django!</h1>
    </body>
    </html>
    '''
    return HttpResponse(texto)

def despedida(request): #Segunda Vista o view
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