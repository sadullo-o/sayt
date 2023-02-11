from django.urls import path
from .views import BlogList, DetailView
urlpatterns = [
    path('blogs', BlogList.as_view()), # domen/api/v1/blogs
    path('blogs/<int:pk>', DetailView.as_view())  # domen/api/v1/blogs/1
 ]