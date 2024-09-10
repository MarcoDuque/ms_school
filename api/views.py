from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models.school import School
from .serializer import SchoolSerializer

# Create your views here.
@api_view(['GET'])
def school_get_all(request):
    school = School.objects.all()
    serializer = SchoolSerializer(school, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def school_find_byId(request, id):
    try:
        school = School.objects.get(id=id)
        serializer = SchoolSerializer(school, many=False)
        return Response(serializer.data)
    except School.DoesNotExist: 
        return Response("School with {id} can't by find")
        
@api_view(['POST'])
def create_school(request):
    serializer = SchoolSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def school_update(request, id):
    
    try:
        school = School.objects.get(pk=id)
        school.school_name = request.data.get('school_name')
        school.school_slogan = request.data.get('school_slogan')
        school.school_address = request.data.get('school_address')
        school.school_city = request.data.get('school_city')
        school.school_state = request.data.get('school_state')
        school.school_zip = request.data.get('school_zip')
        school.school_phone = request.data.get('school_phone')
        school.school_email = request.data.get('school_email')
        school.school_photo_logo = request.data.get('school_photo_logo')
        school.school_users_admin = request.data.get('school_users_admin')
        school.school_users_operators = request.data.get('school_users_operators')
        school.save()
        
        serializer = SchoolSerializer(school, many=False)
        return Response(serializer.data)
    
    except School.DoesNotExist: 
        return Response("School with {id} can't by find to update")
    
@api_view(['DELETE'])
def school_delete(request, id):
    
    try:
        school = School.objects.get(pk=id)
        school.delete()
        
        serializer = SchoolSerializer(school, many=False)
        return Response(serializer.data)
    except School.DoesNotExist: 
        return Response("School with {id} can't by delete")
    
