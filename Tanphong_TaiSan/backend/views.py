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
        return super().get_queryset().filter(trangthai=1).order_by('id_hopdong')

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
        Hopdong_obj = self.get_object()
        Hopdong_obj.trangthai = 0
        Hopdong_obj.save()

        return Response({
            "message":"Xóa thành công"
        }, status=status.HTTP_200_OK)
    

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



class HopDongNhaXuongAPIView(generics.GenericAPIView,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin):
    
    queryset = HopdongNhaxuong.objects.all()
    serializer_class = HopDongNhaXuongSerializer

    def get_queryset(self):
        return super().get_queryset().order_by("id")
    
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, "Tải dữ liệu thành công",*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        serializers_hopdongnhaxuong = self.get_serializer(data = request.data)
        if serializers_hopdongnhaxuong.is_valid():
            serializers_hopdongnhaxuong.save()
            return self.list(request, "Thêm mới thành công",*args, **kwargs)
        return Response({
            "data": None,
            "message": "Định dạng dữ liệu chưa đúng",
            "error": serializers_hopdongnhaxuong.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, *args, **kwargs):
        # Chi data thành 2 phần update và create
        update_data = []
        create_data = []
        for data in request.data:
            if 'id' in data:
                update_data.append(data)
            else: 
                create_data.append(data)

        # Chuyển data về thành serializer
        update_serializer = self.get_serializer(data = update_data)
        create_serializer = self.get_serializer(data = create_data)

        # Update dữ liệu hàng loạt
        if update_serializer.is_valid():
            update_obj = [HopdongNhaxuong(**data) for data in update_serializer.validated_data]
            HopdongNhaxuong.objects.bulk_update(objs=update_obj, fields=[f.name for f in HopdongNhaxuong._meta.fields if f.name != 'id'])

            # Create dữ liệu hàng loạt
            if create_serializer.is_valid():
                create_obj = [HopdongNhaxuong(**data) for data in create_serializer.validated_data]
                HopdongNhaxuong.objects.bulk_create(create_obj)
                return self.list(request, "Cập nhật dữ liệu thành công", *args, **kwargs)
            
            # Responce khi dữ liệu create xác thực sai
            return Response({
                "data":None,
                "message": "Định dạng dữ liệu create chưa đúng chưa đúng",
                "error": create_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        # Responce khi dữ liệu update xác thực sai
        return Response({
            "data":None,
            "message": "Định dạng dữ liệu update chưa đúng chưa đúng",
            "error": update_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

    def list(self, request, message,*args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "data": serializer.data,
            "message": message,
            "error": None
        }, status=status.HTTP_200_OK)



class HopDongDichVu_For_ThanhToanAPIView(APIView):
    """API View xử lý dữ liệu thanh toán dịch vụ từ hợp đồng"""
    
    def get(self, request):
        """Xử lý GET request để lấy và chuẩn bị dữ liệu thanh toán"""
        # Lấy id_hopdong từ query params
        id_hopdong = request.GET.get("id_hopdong")
        
        # Kiểm tra id_hopdong
        if id_hopdong is None:
            return Response({
                "data": None,
                "message": "Thiếu id_hopdong"
            }, status=status.HTTP_400_BAD_REQUEST)
            
        # Lấy bản ghi thanh toán gần nhất
        thanhtoan = ThanhtoanDichvu.objects.filter(id_hopdong=id_hopdong).order_by('-id').first()
        if not thanhtoan:
            return Response({
                "data": [],
                "message": f"Không tìm thấy dữ liệu thanh toán cho hợp đồng {id_hopdong}"
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Chuyển đổi dữ liệu và chuẩn bị cho kỳ thanh toán mới
        data_ky_cu = ThanhtoanDichvuSerializer(thanhtoan).data
        data_ky_moi = []
        
        # Xử lý từng mục thanh toán
        for item in data_ky_cu['thanhtoan']:
            item_moi = item.copy()
            item_moi['chisocu'] = item_moi['chisomoi']  # Chỉ số cũ kỳ này = chỉ số mới kỳ trước
            item_moi['chisomoi'] = None                 # Reset chỉ số mới
            item_moi['soluong'] = item_moi['sosudung']  # Gán số lượng bằng số đã sử dụng
            item_moi['id_dichvu'] = item_moi['dichvu'] # Gán id dịch vụ
            data_ky_moi.append(item_moi)
        
        return Response({
            "data": data_ky_moi,
            "message": "Lấy dữ liệu thành công",
        }, status=status.HTTP_200_OK)



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

class ThanhtoanDichvuMixinsView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = ThanhtoanDichvu.objects.prefetch_related('thanhtoan')
    serializer_class = ThanhtoanDichvuSerializer

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


class CtThanhtoanDichvuMixinsView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = CtThanhtoanDichvu.objects.all()
    serializer_class = CtThanhtoanDichvuSerializer

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