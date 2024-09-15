from rest_framework import serializers
from ..models.subsidiary import Subsidiary

class SubsidiarySerializer(serializers.ModelSerializer):
    subsidiary_photo_logo =  serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Subsidiary
        fields = '__all__'

