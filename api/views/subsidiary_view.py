from rest_framework import viewsets
from ..models.subsidiary import Subsidiary
from ..serializers.subsidiary_serializer import SubsidiarySerializer

class SubsidiaryViewSet(viewsets.ModelViewSet):
    serializer_class = SubsidiarySerializer
    queryset = Subsidiary.objects.all()