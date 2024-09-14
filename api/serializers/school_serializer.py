from rest_framework import serializers
from ..models.school import School

class SchoolSerializer(serializers.ModelSerializer):
    school_photo_logo =  serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = School
        fields = '__all__'

