from django.shortcuts import redirect, render, redirect
from .forms import FormularioContacto
from django.core.mail import send_mail
# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()
    
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            
            try:
                send_mail('Contacto Web Gestion Pedidos',"Usuario: {} \n Email: {} . \n Mensaje: {}".format(nombre,email,contenido),email,['tutossjok@gmail.com'])
                
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
    return render (request, "contacto/contacto.html",{'miFormulario':formulario_contacto})