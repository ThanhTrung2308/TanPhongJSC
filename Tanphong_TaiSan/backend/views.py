from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from .models import *
from .serializer import *

def index(request):
    return HttpResponse("hello world")

# Create your views here.
class HopDongAPIView(generics.GenericAPIView,
                     generics.mixins.ListModelMixin,
                     generics.mixins.CreateModelMixin,
                     generics.mixins.RetrieveModelMixin,
                     generics.mixins.UpdateModelMixin,
                     generics.mixins.DestroyModelMixin):
    queryset = Hopdong.objects.all()
    serializer_class = HopDongSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
    #     if self.request.method == 'POST':
    #         serializer = HopDongSerializer(data=request.data)
    #     else:
    #         serializer = self.get_serializer(data=request.data)

    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status= status.HTTP_201_CREATED, headers=headers)

    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class DichVuAPIView(generics.GenericAPIView,
                     generics.mixins.ListModelMixin,
                     generics.mixins.CreateModelMixin,
                     generics.mixins.RetrieveModelMixin,
                     generics.mixins.UpdateModelMixin,
                     generics.mixins.DestroyModelMixin):
    queryset = Dichvu.objects.all()
    serializer_class = DichVuSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data'), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class HopDongDichVuAPIView(generics.GenericAPIView,
                     generics.mixins.ListModelMixin,
                     generics.mixins.CreateModelMixin,
                     generics.mixins.RetrieveModelMixin,
                     generics.mixins.UpdateModelMixin,
                     generics.mixins.DestroyModelMixin):
    queryset = HopdongDichvu.objects.all()
    serializer_class = HopDongDichVuSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data'), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        data = request.data
        update_data = []
        create_data = []
        for item in data:
            if 'id_hopdongdichvu' in item:
                update_data.append(item)
            else:
                create_data.append(item)
        
        # Update data
        serializer_hopdongdichvu = self.get_serializer(data = update_data)
        if serializer_hopdongdichvu.is_valid():
            hopdongdichvu_obj = [HopdongDichvu(**data) for data in serializer_hopdongdichvu.validated_data]
            HopdongDichvu.objects.bulk_update(objs=hopdongdichvu_obj, fields=[
                'id_hopdong',
                'id_dichvu',
                'dientich_soluong',
                'dongia',
                'chuthich',
            ])
        
        else: return Response(serializer_hopdongdichvu.errors, status=status.HTTP_400_BAD_REQUEST)

        # Create Data
        if create_data:
            serializer_hopdongdichvu = self.get_serializer(data=create_data)
            if serializer_hopdongdichvu.is_valid():
                serializer_hopdongdichvu.save()
            else: return Response(serializer_hopdongdichvu.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response("Cập nhật dữ liệu thành công", status=status.HTTP_200_OK)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class LoaiDichVuAPIView(generics.GenericAPIView,
                     generics.mixins.ListModelMixin,
                     generics.mixins.CreateModelMixin,
                     generics.mixins.RetrieveModelMixin,
                     generics.mixins.UpdateModelMixin,
                     generics.mixins.DestroyModelMixin):
    queryset = Loaidichvu.objects.all()
    serializer_class = LoaiDichVuSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class TaiSanAPIView(generics.GenericAPIView,
                     generics.mixins.ListModelMixin,
                     generics.mixins.CreateModelMixin,
                     generics.mixins.RetrieveModelMixin,
                     generics.mixins.UpdateModelMixin,
                     generics.mixins.DestroyModelMixin):
    queryset = Taisan.objects.all()
    serializer_class = TaiSanSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data'), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)  
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class LoaiTaiSanAPIView(generics.GenericAPIView,
                     generics.mixins.ListModelMixin,
                     generics.mixins.CreateModelMixin,
                     generics.mixins.RetrieveModelMixin,
                     generics.mixins.UpdateModelMixin,
                     generics.mixins.DestroyModelMixin):
    queryset = Loaitaisan.objects.all()
    serializer_class = LoaiTaiSanSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class KheUocVayAPIView(generics.GenericAPIView,
                     generics.mixins.ListModelMixin,
                     generics.mixins.CreateModelMixin,
                     generics.mixins.RetrieveModelMixin,
                     generics.mixins.UpdateModelMixin,
                     generics.mixins.DestroyModelMixin):
    queryset = Kheuocvay.objects.all()
    serializer_class = KheUocVaySerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class HopDongThanhToanMixinsView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = HopdongThanhtoan.objects.all()
    serializer_class = HopDongThanhToanSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk") is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ThanhToanMixinsView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Thanhtoan.objects.all()
    serializer_class = ThanhToanSerializer
    # lookup_field = 'id'

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk") is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer_thanhtoan = self.get_serializer(data = request.data)
        if serializer_thanhtoan.is_valid():
            for validated_data in serializer_thanhtoan.validated_data:
                validated_data['tientruocthue'] = validated_data['dongia'] * validated_data['sosudung'] if validated_data['sosudung'] is not None else validated_data['dongia']
                validated_data['thue'] = validated_data['tientruocthue'] * validated_data['loaithue']/100
                validated_data['tiensauthue'] = validated_data['tientruocthue'] + validated_data['thue']
                
            thanhtoan_obj = [Thanhtoan(**data) for data in serializer_thanhtoan.validated_data]
            Thanhtoan.objects.bulk_create(objs=thanhtoan_obj)
            return self.list(request, *args, **kwargs)
        return Response(serializer_thanhtoan.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, *args, **kwargs):
        serializer_thanhtoan = self.get_serializer(data = request.data)
        if serializer_thanhtoan.is_valid():

            for validated_data in serializer_thanhtoan.validated_data:
                validated_data['tientruocthue'] = validated_data['dongia'] * validated_data['sosudung'] if validated_data['sosudung'] is not None else validated_data['dongia']
                validated_data['thue'] = validated_data['tientruocthue'] * validated_data['loaithue']/100
                validated_data['tiensauthue'] = validated_data['tientruocthue'] + validated_data['thue']

            thanhtoan_obj = [Thanhtoan(**data) for data in serializer_thanhtoan.validated_data]
            Thanhtoan.objects.bulk_update(objs= thanhtoan_obj, fields=[
                'id_hopdongthanhtoan',
                'dichvu',
                'tientruocthue',
                'thue',
                'tiensauthue',
                'donvitinh',
                'chisocu',
                'chisomoi',
                'heso',
                'dongia',
                'sosudung'
            ])
            return self.list(request, *args, **kwargs)
        return Response(serializer_thanhtoan.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)