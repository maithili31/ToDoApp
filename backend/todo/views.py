from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from django.http import HttpResponse


# Create your views here.

def option(request):
    return HttpResponse('<h1> Use admin/ or api/ </h1>')

def home(request):
    return HttpResponse('<h2> Welcome </h2>')

def login(request):
    return HttpResponse('<h2> Please enter your credentials </h2>')

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
