from rest_framework import serializers
from .models import Matakuliah

class MatakuliahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matakuliah
        fields = '__all__'