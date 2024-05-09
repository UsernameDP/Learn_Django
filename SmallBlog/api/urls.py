from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login),
    path("complete/ion", views.completeLogin),
    path("authenticate", views.authenticate),
    path("getPost/<int:id>", views.getPost),
    path("getAllPosts", views.getAllPosts),
    path("addPost", views.addPost),
]
