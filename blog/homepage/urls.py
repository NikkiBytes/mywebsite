from django.urls import path
from . import views
from homepage.views import HomeView, AboutMeView, LabsView, BlogView, ContactView


urlpatterns = [
    path('', HomeView.as_view(), name='index')


]
