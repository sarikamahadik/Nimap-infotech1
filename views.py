from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Client, Project
from .serializer import ClientSerializer, ProjectSerializer


class ClientList(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    def get_queryset(self):
        queryset = Client.objects.all()
        project = self.request.query_params.get('project')
        if project is not None:
            queryset = queryset.filter(clientProject=project)
        return queryset

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()