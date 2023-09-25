from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista1(request):
    html = "<h1 style='text-align:center; color:blue;'> Aplicacion 1 </h1>"
    return HttpResponse(html)

def vista3(request):
    html = """
    <div>
        <h1 style='text-align:center; color:blue;'> Aplicacion 1 </h1>
        <p> <b> vista 3 </b> </p>
    </div>
    """
    return HttpResponse(html)