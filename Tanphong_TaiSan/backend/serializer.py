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
    
class HopDongDichVuSerializer(serializers.ModelSerializer):
    class Meta:
        model = HopdongDichvu
        fields = "__all__"
        extra_kwargs = {
            'id_hopdongdichvu': {'read_only': False, 'required': False}
        }

class LoaiDichVuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loaidichvu
        fields = "__all__"

class TaiSanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taisan
        fields = "__all__"

class LoaiTaiSanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loaitaisan
        fields = "__all__"

class KheUocVaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Kheuocvay
        fields = "__all__"
    
class HopDongThanhToanSerializer(serializers.ModelSerializer):
    class Meta:
        model = HopdongThanhtoan
        fields = "__all__"

class ThanhToanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thanhtoan
        fields = "__all__"
        extra_kwargs = {
            'id': {'read_only': False, 'required': False}
        }