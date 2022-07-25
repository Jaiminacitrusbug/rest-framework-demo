from django.shortcuts import render
from django.views import View
from apps.models import Blog
from rest_framework import serializers, viewsets

# Create your views here.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ['name', 'desc']
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = UserSerializer


# class Blogs(View):   
#     def get(self, request): 
#       print("Blogs")