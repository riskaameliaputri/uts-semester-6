from rest_framework import viewsets
from .models import Matakuliah
from .serializers import MatakuliahSerializer

class MatakuliahViewSet(viewsets.ModelViewSet):
    queryset = Matakuliah.objects.all()
    serializer_class = MatakuliahSerializer

