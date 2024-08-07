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

    def get_queryset(self):
        return super().get_queryset().order_by('id_hopdong')

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

    def get_queryset(self):
        return super().get_queryset().order_by("id_dichvu")

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
        print(request.GET)
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
                'soluong',
                'donvitinh',
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

class HopDongDichVu_For_ThanhToanAPIView(APIView):
    def get(self, request):
        param_query = request.GET.get("id_hopdong")
        print(request.GET)
        if param_query is not None:
            hopdongdichvu = HopdongDichvu.objects.filter(id_hopdong=param_query)
            serializers_hopdongdichvu = HopDongDichVuSerializer(hopdongdichvu, many=True)

            hopdongthanhtoan = HopdongThanhtoan.objects.order_by('-id').first()
            serializers_hopdongthanhtoan = HopDongThanhToanSerializer(hopdongthanhtoan)
            
            # Tạo một bản sao của dữ liệu để có thể sửa đổi
            updated_data = []
            
            for field_hddv in serializers_hopdongdichvu.data:
                updated_field = field_hddv.copy()  # Tạo bản sao của mỗi phần tử
                for filed_tt in serializers_hopdongthanhtoan.data['thanhtoan']:
                    if field_hddv['id_dichvu'] == filed_tt['dichvu']:
                        updated_field['chisocu'] = filed_tt['chisomoi']
                updated_data.append(updated_field)
            return Response({
                "data:":updated_data,
                "message": "successfully",
            }, status=status.HTTP_200_OK)

        return Response({
            "data": None,
            "message": "Không có query id" 
        }, status=status.HTTP_400_BAD_REQUEST)



class LoaiDichVuAPIView(generics.GenericAPIView,
                     generics.mixins.ListModelMixin,
                     generics.mixins.CreateModelMixin,
                     generics.mixins.RetrieveModelMixin,
                     generics.mixins.UpdateModelMixin,
                     generics.mixins.DestroyModelMixin):
    queryset = Loaidichvu.objects.all()
    serializer_class = LoaiDichVuSerializer

    def get_queryset(self):
        return super().get_queryset().order_by("id_loaidichvu")

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

    def get_queryset(self):
        return super().get_queryset().order_by("id")

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
        file = request.FILES.get('file')  # Get the uploaded file from request.FILES
        email_send = request.data.get("email")

        if file:
            email = EmailMessage(
                subject="Test Send Mail",
                body="Test đính kèm file",
                from_email='adudarkwa33@gmail.com',
                to=[email_send],
            )

            # Attach the file to the email
            email.attach(file.name, file.read(), file.content_type)
            email.send()

            return Response({
                "message": "File sent successfully"
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "No file provided"
        }, status=status.HTTP_400_BAD_REQUEST)