from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Gustavo Mundo")

def segundaVista(request):
    return HttpResponse("<br><br>------Ya somos programadores web -----")

def dia(request):
    variable = datetime.now()
    return HttpResponse(f"Hoy es un gran dia <br>{variable}")

def apellido(request, ape):
    fecha = datetime.now()
    return HttpResponse(f"Este alumno de Coder {ape}, es muy bueno..<br><br>..Por lo menos el dia de hoy:{fecha}")

def cuantosAniosTengo(request, edad):
    fecha = datetime.now()
    anio = int(edad)-fecha.year
    return HttpResponse(f"Tengo {edad} años de edad y naci en el {anio} <br><br>{fecha}")

def probandoTemplate(request):
    with open("C:/Users/gdiaz/OneDrive/GOOGLE DRIVE/Gustavo/Curso programacion/Coder House/play Ground/DjangoTest1/Proyecto1/Proyecto1/Plantillas/template1.html") as miHTML:
        plantilla = Template(miHTML.read())
    miContexto = Context({"nombre": "Gustavo", "apellido": "Diaz", "edad": "22"})
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)