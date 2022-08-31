from django.urls import path
from post.views import home
urlpatterns = [
    path("",home,name="home")
]