from django.http import HttpResponse
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage

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
    queryset = HopdongThanhtoan.objects.prefetch_related('thanhtoan')
    serializer_class = HopDongThanhToanSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk") is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        so_tbdv = request.data.get('sotbdv')
        if self.queryset.filter(sotbdv = so_tbdv).exists():
            return Response({
                "data": None,
                "message": "Đã tồn tại mã" 
            }, status=status.HTTP_400_BAD_REQUEST)
        
        serializer_hopdongthanhtoan = self.get_serializer(data = request.data)
        if serializer_hopdongthanhtoan.is_valid():
            serializer_hopdongthanhtoan.save()
            return self.list(request, *args, **kwargs)
        
        return Response({
            "data": None,
            "message": serializer_hopdongthanhtoan.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        try:
            hopdongthanhtoan_obj = self.queryset.get(id=request.data.get('id'))
        except ObjectDoesNotExist:
            return Response({
                "data": None,
                "message": "Không tìm thấy hợp đồng thanh toán với id này"
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer_hopdongthanhtoan = self.get_serializer(hopdongthanhtoan_obj, data = request.data)
        if serializer_hopdongthanhtoan.is_valid():
            serializer_hopdongthanhtoan.save()
            return self.list(request, *args, **kwargs)
        
        return Response({
            "data": None,
            "message": serializer_hopdongthanhtoan.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
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

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk") is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class SendMailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        pdf_file = request.data.get('file')
        email = EmailMessage(
            subject="Test Send Mail",
            body="Test đính k",
            from_email='adudarkwa33@gmail.com',
            to=['thanhd436@gmail.com'],
        )

        # Attach the PDF file to the email
        email.attach('invoice.pdf', pdf_file.read(), 'application/pdf')
        email.send()

        return Response({
            "data":None,
            "Message": "Gửi File Thành Công"
        }, status=status.HTTP_200_OK)