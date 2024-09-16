from django.shortcuts import render
from rest_framework import viewsets
from ..models.school import School
from ..serializers.school_serializer import SchoolSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    
    def list(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'api':
            return render(request, 'school_list.html', {'schools': self.get_queryset()})
        return super(SchoolViewSet, self).list(request, *args, **kwargs)