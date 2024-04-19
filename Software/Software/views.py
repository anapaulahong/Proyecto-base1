from django.shortcuts import render

def formulario_preguntas(request):
    return render(request, 'formulario_preguntas.html')