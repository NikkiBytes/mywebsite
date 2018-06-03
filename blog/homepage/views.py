from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'homepage.html')
#    template = loader.get_template('aboutme.html')
#    return HttpResponse(template.render(request, template, context=None))
# Create your views here.
