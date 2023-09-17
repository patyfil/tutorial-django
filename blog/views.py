from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html')
def sobre(request):
    return render(request, 'blog/sobre.html')
def contato(request):
    return render(request, 'blog/contato.html')