from django.urls import path
from . import views
from homepage.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='index')


]
