from django.urls import path
from . import views
from homepage.views import HomeView, AboutMeView, LabsView, BlogView, ContactView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutMeView.as_view(), name="about"),
    path('labs/', LabsView.as_view(), name='labs'),
    path('blog/', BlogView.as_view(), name="blog"),
    path('contact/', ContactView.as_view(), name="contact")


]
