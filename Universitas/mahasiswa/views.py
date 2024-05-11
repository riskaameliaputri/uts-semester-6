from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Mahasiswa
from .serializers import MahasiswaSerializer

@api_view(['GET', 'POST'])
def Mahasiswa_list(request):
    if request.method == 'GET':
        mahasiswa = Mahasiswa.objects.all()
        serializer = MahasiswaSerializer(mahasiswa, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
       serializer == MahasiswaSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
