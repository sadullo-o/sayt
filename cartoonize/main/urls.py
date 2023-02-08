from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),  # 127.0.0.1:8000
    path('result', result, name='result'),

]