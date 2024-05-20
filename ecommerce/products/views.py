from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# views : Request Handler, functions, takes request as parameter and return to Http response. 

def index(request): 
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def create(request):
    return render(request, "create.html")