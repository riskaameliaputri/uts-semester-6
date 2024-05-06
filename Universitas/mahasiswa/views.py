from rest_framework import viewsets
from .models import Mahasiswa
from .serializers import MahasiswaSerializer

class MahasiswaViewSet(viewsets.ModelViewSet):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer
