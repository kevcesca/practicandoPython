from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Curso
from .forms import CursoFormulario

# Create your views here.
def curso(req, nombre, camada):
    
    curso = Curso(nombre = nombre, camada = camada)
    curso.save()
    
    return HttpResponse(f""" 
                <p>Curso: {curso.nombre} <br> Camada: {curso.camada} </p>
            """)

def lista_cursos(req):
    
    lista = Curso.objects.all()
    
    return  render(req, "lista_cursos.html", {"lista_cursos" : lista})

def inicio (req):
    
    return render(req, "inicio.html")

def cursos (req):
    return render(req, "cursos.html")


def profesores (req):
    return render(req, "profesores.html")



def estudiantes (req):
    return render(req, "estudiantes.html")


def entregables (req):
    return render(req, "entregables.html")


def curso_formulario(req: HttpRequest):
    print("method", req.method)
    print("post", req.POST)
    
    if req.method == "POST":
        
        miFormulario = CursoFormulario(req.POST)
        
        if miFormulario.is_valid():
            
            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data
            
            curso = Curso(nombre = data["curso"], camada = data["camada"])
            curso.save()
            return render(req, "inicio.html", {"mensaje": "Curso Creado con exito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        miFormulario = CursoFormulario()
        
        return render(req, "cursoFormulario.html", {"miFormulario": miFormulario})


def busqueda_camada(req):
    return render(req, "busquedaCamada.html")

def buscar(req):
    
    if req.GET["camada"]:
        camadaBuscada = req.GET["camada"]
        curso = Curso.objects.get(camada = camadaBuscada)
        if curso:
            return render(req, "resultadoBusqueda.html", {"curso": curso})
    else:
        return HttpResponse(f"No escribiste la camada")