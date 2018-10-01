from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView, RedirectView



class HomeView(TemplateView):
    template_name = 'modern_design.html'
class AboutMeView(TemplateView):
    template_name = 'aboutme.html'
class LabsView(TemplateView):
    template_name = "labview.html"
class BlogView(TemplateView):
    template_name = "blogview.html"
class ContactView(TemplateView):
    template_name = "contact.html"
