from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login, name="login"), #This redirects you to the ion login page
    path("addPost", views.addPost, name="addPost"),
    path("getPost", views.getPost, name="getPost"),
    path("getAllPosts", views.getAllPosts, name="getAllPosts"),
    path("complete/ion", views.authenticate, name="authenticate"), #this is where you recieve the token after /api/login was successful
    path("test", views.test, name="test"),
]