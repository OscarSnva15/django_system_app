#django tiene mucho modulos, que podemos utilizar
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. send files html
def hello(request):
    return HttpResponse("<h2>Hello Word</h2>")


def about(request):
    return HttpResponse("about page")
