from rest_framework import viewsets
from .models import Nilai
from .serializers import NilaiSerializer

class NilaiViewSet(viewsets.ModelViewSet):
    queryset = Nilai.objects.all()
    serializer_class = NilaiSerializer
