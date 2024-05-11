from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Nilai
from .serializers import NilaiSerializer


@api_view(['GET', 'POST'])
def Nilai_list(request,format=None):
    if request.method == 'GET':
        nilai = Nilai.objects.all()
        serializer = NilaiSerializer(nilai, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer =NilaiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)