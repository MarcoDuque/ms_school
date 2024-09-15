from rest_framework import viewsets
from ..models.school import School
from ..serializers.school_serializer import SchoolSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
