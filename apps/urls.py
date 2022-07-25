from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
      path('', views.UserViewSet, name="Blogs"),
    
]
app_name='blog'