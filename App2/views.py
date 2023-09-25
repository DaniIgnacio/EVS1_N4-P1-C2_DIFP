from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista2(request):
    html = "<h1 style='text-align:center; color:red;'> Aplicacion 2 </h1>"
    return HttpResponse(html)


def vista4(request):
    html = """
    <div>
        <h1 style='text-align:center; color:red;'> Aplicacion 2 </h1>
        <p> <b> vista 4 </b> </p>
    </div>
    """
    return HttpResponse(html)