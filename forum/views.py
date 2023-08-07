from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import EntradaFormulario
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    titulo = "Esto es una prueba de plantillas"
    return render(request,'home.html', {
        'titulo': titulo
    })

def busquedaPosts(request):
    nombre = request.GET['post']

    resultadoBusqueda = EntradaFormulario.objects.filter(titulo__icontains=nombre)

    return render(request,'verPosts.html',{
        'posts' : resultadoBusqueda
    })

def verPosts(request):
    posts = EntradaFormulario.objects.all()
    return render(request,'verPosts.html',{
        'posts': posts
    })

def postRead(request):
    post = EntradaFormulario.objects.get(id=request.GET['id'])
    return render(request,'postRead.html',{
        'post': post
    })

@login_required
def crearPost(request):
    if request.method == 'GET':
        if request.GET['id'] != '-1':
            postOriginal =  EntradaFormulario.objects.get(id=request.GET['id'])
            return render(request,'crearPost.html',{
                'postOriginal': postOriginal
            })
        else:
            return render(request,'crearPost.html')
    else:
        if request.POST['editar'] == '-1':
            # create the post
            post = EntradaFormulario(titulo=request.POST['titulo'],cuerpo=request.POST['cuerpo'],user=request.user)
            post.save()
        else:
            post = EntradaFormulario.objects.get(id=request.POST['editar'])
            post.titulo = request.POST['titulo']
            post.cuerpo = request.POST['cuerpo']
            post.save()
        # redirect the user to the post
        return redirect('/verPosts')

@login_required
def eliminarPost(request):
    postOriginal =  EntradaFormulario.objects.get(id=request.GET['id'])
    postOriginal.delete()
    return redirect('/verPosts')
