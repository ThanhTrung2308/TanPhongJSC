from django.urls import path

from . import views

urlpatterns = [
    path('hopdong/',views.HopDongAPIView.as_view()),
    path('dichvu/',views.DichVuAPIView.as_view()),
    path('hopdongdichvu/',views.HopDongDichVuAPIView.as_view()),
    path('loaidichvu/',views.LoaiDichVuAPIView.as_view()),
    path('taisan/',views.TaiSanAPIView.as_view()),
    path('loaitaisan/',views.LoaiTaiSanAPIView.as_view()),
    path('',views.index)
]
