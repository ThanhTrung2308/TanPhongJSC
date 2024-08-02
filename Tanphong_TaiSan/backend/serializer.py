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

class ThanhToanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thanhtoan
        fields = "__all__"
        extra_kwargs = {
            'id': {'read_only': False, 'required': False}
        }

class HopDongThanhToanSerializer(serializers.ModelSerializer):
    thanhtoan = ThanhToanSerializer(many = True)
    tongtiensauthue_giamtru = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = HopdongThanhtoan
        fields = "__all__"
    
    def create(self, validated_data):
        thanhtoan_data = validated_data.pop('thanhtoan')
        for data in thanhtoan_data:
            data['tientruocthue'] = data['dongia'] * data['sosudung'] if data['sosudung'] is not None else validated_data['dongia']
            data['thue'] = data['tientruocthue'] * data['loaithue']/100
            data['tiensauthue'] = data['tientruocthue'] + data['thue']
        
        validated_data['tongtientruocthue'] = sum(data['tientruocthue'] for data in thanhtoan_data)
        validated_data['tongtiensauthue'] = sum(data['tiensauthue'] for data in thanhtoan_data)
        validated_data['giamtru'] = (validated_data['giamtru']/100)*validated_data['tongtientruocthue']

        hopdongthanhtoan_obj = HopdongThanhtoan.objects.create(**validated_data)
        
        for data in thanhtoan_data:
            Thanhtoan.objects.create(id_hopdongthanhtoan = hopdongthanhtoan_obj, **data)
        return hopdongthanhtoan_obj
    
    def update(self, instance, validated_data):
        thanhtoan_data = validated_data.pop('thanhtoan')
        for data in thanhtoan_data:
            data['tientruocthue'] = data['dongia'] * data['sosudung'] if data['sosudung'] is not None else validated_data['dongia']
            data['thue'] = data['tientruocthue'] * data['loaithue']/100
            data['tiensauthue'] = data['tientruocthue'] + data['thue']

        update_data = []
        create_data = []
        for data in thanhtoan_data:
            if 'id' in data: 
                update_data.append(data)
            else: 
                create_data.append(data)

        # Update Hopdongthanhtoan
        validated_data['tongtientruocthue'] = sum(data['tientruocthue'] for data in thanhtoan_data)
        validated_data['tongtiensauthue'] = sum(data['tiensauthue'] for data in thanhtoan_data)
        validated_data['giamtru'] = (validated_data['giamtru']/100)*validated_data['tongtientruocthue']

        # Update thanhtoan
        field_names = [field.name for field in Thanhtoan._meta.fields if field.name != 'id']
        thanhtoan_obj = [Thanhtoan(**data) for data in update_data]
        Thanhtoan.objects.bulk_update(objs=thanhtoan_obj, fields=field_names)

        # Create thanhtoan
        thanhtoan_obj = [Thanhtoan(**data) for data in create_data]
        Thanhtoan.objects.bulk_create(objs=thanhtoan_obj)
        
        return super().update(instance, validated_data)
    
    def get_tongtiensauthue_giamtru(self, obj):
        return obj.tongtiensauthue - obj.giamtru
        
        

