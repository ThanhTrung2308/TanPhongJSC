from rest_framework import serializers
from .models import *

class HopDongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hopdong
        fields = [
            "ten",
            "sohd",
            "thoigianthue",
            "kythanhtoan_thang_lan_field",
            "tongthu",
            "chuthich",
            "ngayghi"
        ]


class DichVuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dichvu
        fields = [
            "tendichvu",
            "chuthich",
            "ngayghi",
            "id_loaidichvu"
        ]
    
class HopDongDichVuSerializer(serializers.ModelSerializer):
    class Meta:
        model = HopdongDichvu
        fields = [
                "dientich_soluong",
                "dongia",
                "chuthich",
                "id_hopdong",
                "id_dichvu"
        ]

class LoaiDichVuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loaidichvu
        fields = [
                "tenloaidichvu",
                "chuthich"
        ]

class TaiSanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taisan
        fields = [
                "tentaisan",
                "ngayghitang",
                "thoigiansudung",
                "nguyengia",
                "chuthich",
                "id_loaitaisan"
        ]

class LoaiTaiSanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loaitaisan
        fields = [
                "tenloaitaisan",
                "chuthich"
            ]

class KheUocVaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Kheuocvay
        fields = ["makheuoc",
                    "tenkheuoc",
                    "sotienvay",
                    "laisuat_nam",
                    "ngayvay",
                    "thoigianvay",
                    "hinhthuctravay",
                    "chuthich"]