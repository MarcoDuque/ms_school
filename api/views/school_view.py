from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from api.models.subsidiary import Subsidiary
from rest_framework.response import Response
from ..models.school import School
from ..serializers.school_serializer import SchoolSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    subsidiary = Subsidiary.objects.all()
    
    school = {
        'school': queryset,
        'subsidiary': subsidiary
    }
    
    def list(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'api':
            return render(request, 'school_list.html', self.school)
        return super(SchoolViewSet, self).list(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        try:
            school = get_object_or_404(School,id=kwargs.get('pk'))
            if (school.school_active == False):
                return Response({"error": 'School is not active' },
                            status=status.HTTP_400_BAD_REQUEST)
            else:    
                school.school_active = False
                school.save()
            return Response({"message": "School Marked as inactive"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e.args)}, status=status.HTTP_400_BAD_REQUEST)
