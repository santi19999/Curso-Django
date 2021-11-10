from django.http import HttpResponse

#Siempre deben retornar el httpResponse y deben resibir como parámetro el request


def saludo(request):  #Primera Vista o view
    return HttpResponse("Hola alumnos esta es nuestra primera página con django")

def despedida(request): #Segunda Vista o view
    return HttpResponse("Hasta Luego Alumnos de Django")