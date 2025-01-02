from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Project, ProjectMember, Task, Comment
from .serializers import UserSerializer, ProjectSerializer
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect('/swagger/')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


