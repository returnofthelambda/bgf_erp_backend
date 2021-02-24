from django.shortcuts import render

from rest_framework import generics

from .serializers import ContainerListSerializer, ContainerDetailSerializer
from .models import Container


class ContainerListAPIView(generics.ListAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerListSerializer


class ContainerRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Container.objects.all()
    serializer_class = ContainerDetailSerializer


# Create form does not filter Booking choices by steamship.
class ContainerCreateAPIView(generics.CreateAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerDetailSerializer


class ContainerRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Container.objects.all()
    serializer_class = ContainerDetailSerializer


class ContainerDestroyAPIView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Container.objects.all()
