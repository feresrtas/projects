from django.shortcuts import render
from .models import Todo, Category
from .serializers import TodoSerializers, CategorySerializers

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class TodoMVS(ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializers

class CategoryListCreate(ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializers

class CategoryUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializers
    lookup_field ="id"
