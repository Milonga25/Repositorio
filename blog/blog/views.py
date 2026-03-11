from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def acerca_de_nosotros(request):
    return render(request, 'acerca_de_nosotros.html')