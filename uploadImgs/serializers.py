from rest_framework import serializers
from . models import Pictures


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = '__all__'