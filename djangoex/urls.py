from django.contrib import admin
from django.urls import path, include
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('articles/', include("articles.urls")),
    path('users/', include("users.urls"))


]