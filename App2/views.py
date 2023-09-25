from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista2(request):
    html = "<h1 style='text-align:center; color:red;'> Aplicacion 2 </h1>"
    return HttpResponse(html)