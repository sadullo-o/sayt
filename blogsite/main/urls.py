from django.urls import path
# from .views import BlogList, DetailView, Userlist, UserDetail
from .views import UserView, BlogsView
from rest_framework.routers import SimpleRouter

# urlpatterns = [
#     path('blogs', BlogList.as_view()), # domen/api/v1/blogs
#     path('blogs/<int:pk>', DetailView.as_view()),  # domen/api/v1/blogs/1
#     path('users/', Userlist.as_view()),
#     path('users/<int:pk>', UserDetail.as_view())
#
#  ]

router = SimpleRouter()
router.register('users', UserView, basename='users')

router.register('blogs', BlogsView, basename='blogs')

urlpatterns = router.urls


# pip install pyyaml uritemplate  --> sxema

#  pip install drf-yasg  --> dokumentatsiya