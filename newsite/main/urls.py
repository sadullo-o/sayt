from django.urls import path
from .views import main, about, contact


urlpatterns = [
    path('', main, name='main'),  # 127.0.0.1:8000
    path('about', about, name='about'),  # 127.0.0.1:8000/about
    path('contact', contact, name='contact') # 127.0.0.1:8000/contact
]