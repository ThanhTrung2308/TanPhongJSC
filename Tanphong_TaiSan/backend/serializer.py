from rest_framework import serializers
from .models import *

class HopDongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hopdong
        fields = "__all__"


class DichVuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dichvu
        fields = "__all__"