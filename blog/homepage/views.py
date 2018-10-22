from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView, RedirectView



class HomeView(TemplateView):
    template_name = 'modern_design.html'
