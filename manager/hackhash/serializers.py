from rest_framework import serializers
from .models import Hash


class HashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hash
        fields = ["status", "data"]
