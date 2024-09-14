from django.shortcuts import get_object_or_404, render
from rest_framework.exceptions import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from ..models.school import School
from ..serializers.school_serializer import SchoolSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
