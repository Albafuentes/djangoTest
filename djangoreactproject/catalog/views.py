from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    title = "title de prueba"
    return HttpResponse(title)

def form(request):
    title = "title de prueba"
    context = { "title": title }
    return render(request, 'form.html', context=context)
