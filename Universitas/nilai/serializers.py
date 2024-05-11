from rest_framework import serializers
from .models import Nilai

class NilaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nilai
        fields = ["name", "npm_id"]