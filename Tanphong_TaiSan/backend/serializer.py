from rest_framework import serializers
from .models import *


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


class HopDongNhaXuongSerializer(serializers.ModelSerializer):
    class Meta:
        model = HopdongNhaxuong
        fields = "__all__"
        extra_kwargs = {
            'id': {'read_only': False, 'required': False}
        }

class HopDongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hopdong
        fields = "__all__"
    
    def create(self, validated_data):
        print(validated_data)
        validated_data['trangthai'] = 1
        validated_data['tongthu'] = 0
        # return super().create(validated_data)

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

class CtThanhtoanDichvuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CtThanhtoanDichvu
        fields = "__all__"
        extra_kwargs = {
            'id': {'read_only': False, 'required': False}
        }

class ThanhtoanDichvuSerializer(serializers.ModelSerializer):
    thanhtoan = CtThanhtoanDichvuSerializer(many = True)
    tongtiensauthue_giamtru = serializers.SerializerMethodField(read_only = True)
    tien_giamtru = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = ThanhtoanDichvu
        fields = "__all__"
    
    def create(self, validated_data):
        thanhtoan_data = validated_data.pop('thanhtoan')
        for data in thanhtoan_data:
            data['tientruocthue'] = data['dongia'] * data['sosudung'] if data['sosudung'] is not None else validated_data['dongia']
            data['thue'] = data['tientruocthue'] * data['loaithue']/100
            data['tiensauthue'] = data['tientruocthue'] + data['thue']
        
        validated_data['tongtientruocthue'] = sum(data['tientruocthue'] for data in thanhtoan_data)
        validated_data['tongtiensauthue'] = sum(data['tiensauthue'] for data in thanhtoan_data)
        # validated_data['giamtru'] = (validated_data['giamtru']/100)*validated_data['tongtientruocthue']

        hopdongthanhtoan_obj = ThanhtoanDichvu.objects.create(**validated_data)
        
        for data in thanhtoan_data:
            CtThanhtoanDichvu.objects.create(id_hopdongthanhtoan = hopdongthanhtoan_obj, **data)

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
        # validated_data['giamtru'] = (validated_data['giamtru']/100)*validated_data['tongtientruocthue']
        
        # Update thanhtoan
        field_names = ['dichvu', 'tientruocthue', 'thue', 'tiensauthue', 'donvitinh', 'chisocu', 'chisomoi', 'heso', 'dongia', 'sosudung', 'loaithue'] 
        thanhtoan_obj = [CtThanhtoanDichvu(**data) for data in update_data]
        CtThanhtoanDichvu.objects.bulk_update(objs=thanhtoan_obj, fields=field_names)

        # Create thanhtoan
        thanhtoan_obj = [CtThanhtoanDichvu(**data) for data in create_data]
        CtThanhtoanDichvu.objects.bulk_create(objs=thanhtoan_obj)
        
        return super().update(instance, validated_data)
    
    def get_tongtiensauthue_giamtru(self, obj):
        return obj.tongtiensauthue - self.get_tien_giamtru(obj)
    
    def get_tien_giamtru(self, obj):
        return (obj.giamtru/100)*obj.tongtientruocthue
        
        

