from rest_framework import serializers
from .models import *

# class HopDongCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Hopdong
#         fields = [
#             "ten",
#             "sohd",
#             "thoigianthue",
#             "kythanhtoan_thang_lan_field",
#             "tongthu",
#             "chuthich",
#             "ngayghi"
#         ]

class HopDongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hopdong
        fields = "__all__"
    # def create(self, validated_data):
    #     print(validated_data)
    #     #validated_data.pop("id_hopdong")
    #     return Hopdong.objects.create(**validated_data)

class DichVuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dichvu
        fields = "__all__"
    
class HopDongDichVuSerializer(serializers.ModelSerializer):
    class Meta:
        model = HopdongDichvu
        fields = "__all__"

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