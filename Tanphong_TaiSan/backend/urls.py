from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),

    path('hopdong/',views.HopDongAPIView.as_view(),name = 'hopdong-list-create'),
    path('hopdong',views.HopDongAPIView.as_view(),name = 'hopdong-list-create'),

    path('hopdong/<int:pk>/',views.HopDongAPIView.as_view(),name = 'hopdong-update'),
    path('hopdong/<int:pk>',views.HopDongAPIView.as_view(),name = 'hopdong-update'),

    path('hopdong/<int:pk>/',views.HopDongAPIView.as_view(),name = 'hopdong-delete'),
    path('hopdong/<int:pk>',views.HopDongAPIView.as_view(),name = 'hopdong-delete'),

    path('hopdong/<int:pk>/',views.HopDongAPIView.as_view(),name = 'hopdong-retrieve'),
    path('hopdong/<int:pk>',views.HopDongAPIView.as_view(),name = 'hopdong-retrieve'),

    path('dichvu/',views.DichVuAPIView.as_view(),name = 'dichvu-list-create'),
    path('dichvu',views.DichVuAPIView.as_view(),name = 'dichvu-list-create'),

    path('dichvu/<int:pk>/',views.DichVuAPIView.as_view(),name = 'dichvu-update'),
    path('dichvu/<int:pk>',views.DichVuAPIView.as_view(),name = 'dichvu-update'),

    path('dichvu/<int:pk>/',views.DichVuAPIView.as_view(),name = 'dichvu-delete'),
    path('dichvu/<int:pk>',views.DichVuAPIView.as_view(),name = 'dichvu-delete'),

    path('dichvu/<int:pk>/',views.DichVuAPIView.as_view(),name = 'dichvu-retrieve'),
    path('dichvu/<int:pk>',views.DichVuAPIView.as_view(),name = 'dichvu-retrieve'),

    path('hopdongdichvu/',views.HopDongDichVuAPIView.as_view(),name = 'hopdongdichvu-list-create'),
    path('hopdongdichvu',views.HopDongDichVuAPIView.as_view(),name = 'hopdongdichvu-list-create'),

    path('hopdongdichvu/<int:pk>/',views.HopDongDichVuAPIView.as_view(),name = 'hopdongdichvu-update'),
    path('hopdongdichvu/<int:pk>',views.HopDongDichVuAPIView.as_view(),name = 'hopdongdichvu-update'),

    path('hopdongdichvu/<int:pk>/',views.HopDongDichVuAPIView.as_view(),name = 'hopdongdichvu-delete'),
    path('hopdongdichvu/<int:pk>',views.HopDongDichVuAPIView.as_view(),name = 'hopdongdichvu-delete'),

    path('hopdongdichvu/<int:pk>/',views.HopDongDichVuAPIView.as_view(),name = 'hopdongdichvu-retrieve'),
    path('hopdongdichvu/<int:pk>',views.HopDongDichVuAPIView.as_view(),name = 'hopdongdichvu-retrieve'),

    path('hopdongdichvu/update/',views.HopDongDichVuAPIView.as_view(),name = 'hopdongdichvu-update-many'),
    path('hopdongdichvu/update',views.HopDongDichVuAPIView.as_view(),name = 'hopdongdichvu-update-many'),

    path('loaidichvu/',views.LoaiDichVuAPIView.as_view(),name = 'loaidichvu-list-create'),
    path('loaidichvu',views.LoaiDichVuAPIView.as_view(),name = 'loaidichvu-list-create'),

    path('loaidichvu/<int:pk>/',views.LoaiDichVuAPIView.as_view(),name = 'dichvu-update'),
    path('loaidichvu/<int:pk>',views.LoaiDichVuAPIView.as_view(),name = 'dichvu-update'),

    path('loaidichvu/<int:pk>/',views.LoaiDichVuAPIView.as_view(),name = 'dichvu-delete'),
    path('loaidichvu/<int:pk>',views.LoaiDichVuAPIView.as_view(),name = 'dichvu-delete'),

    path('loaidichvu/<int:pk>/',views.LoaiDichVuAPIView.as_view(),name = 'dichvu-retrieve'),
    path('loaidichvu/<int:pk>',views.LoaiDichVuAPIView.as_view(),name = 'dichvu-retrieve'),

    path('taisan/',views.TaiSanAPIView.as_view(), name = 'taisan-list-create'),
    path('taisan',views.TaiSanAPIView.as_view(), name = 'taisan-list-create'),

    path('taisan/<int:pk>/',views.TaiSanAPIView.as_view(), name = 'taisan-update'),
    path('taisan/<int:pk>',views.TaiSanAPIView.as_view(), name = 'taisan-update'),

    path('taisan/<int:pk>/',views.TaiSanAPIView.as_view(), name = 'taisan-delete'),
    path('taisan/<int:pk>',views.TaiSanAPIView.as_view(), name = 'taisan-delete'),

    path('taisan/<int:pk>/',views.TaiSanAPIView.as_view(), name = 'taisan-retrieve'),
    path('taisan/<int:pk>',views.TaiSanAPIView.as_view(), name = 'taisan-retrieve'),

    path('loaitaisan/',views.LoaiTaiSanAPIView.as_view(), name = 'loaitaisan-list-create'),
    path('loaitaisan',views.LoaiTaiSanAPIView.as_view(), name = 'loaitaisan-list-create'),

    path('loaitaisan/<int:pk>/',views.LoaiTaiSanAPIView.as_view(), name = 'loaitaisan-update'),
    path('loaitaisan/<int:pk>',views.LoaiTaiSanAPIView.as_view(), name = 'loaitaisan-update'),

    path('loaitaisan/<int:pk>/',views.LoaiTaiSanAPIView.as_view(), name = 'loaitaisan-delete'),
    path('loaitaisan/<int:pk>',views.LoaiTaiSanAPIView.as_view(), name = 'loaitaisan-delete'),

    path('loaitaisan/<int:pk>/',views.LoaiTaiSanAPIView.as_view(), name = 'loaitaisan-retrieve'),
    path('loaitaisan/<int:pk>',views.LoaiTaiSanAPIView.as_view(), name = 'loaitaisan-retrieve'),

    path('kheuocvay/',views.KheUocVayAPIView.as_view(),name = 'kheuocvay-list-create'),
    path('kheuocvay',views.KheUocVayAPIView.as_view(),name = 'kheuocvay-list-create'),

    path('kheuocvay/<int:pk>/',views.KheUocVayAPIView.as_view(), name ='kheuocvay-update'),
    path('kheuocvay/<int:pk>',views.KheUocVayAPIView.as_view(), name ='kheuocvay-update'),

    path('kheuocvay/<int:pk>/',views.KheUocVayAPIView.as_view(), name ='kheuocvay-delete'),
    path('kheuocvay/<int:pk>',views.KheUocVayAPIView.as_view(), name ='kheuocvay-delete'),

    path('kheuocvay/<int:pk>/',views.KheUocVayAPIView.as_view(), name ='kheuocvay-retrieve'),
    path('kheuocvay/<int:pk>',views.KheUocVayAPIView.as_view(), name ='kheuocvay-retrieve'),

    path("thanhtoan/<int:pk>", views.ThanhToanMixinsView.as_view(), name="thanhtoan-retrieve-delete"),

    path("hopdongthanhtoan/", views.HopDongThanhToanMixinsView.as_view(), name = 'hopdongthanhtoan-list-create-update'),
    path("hopdongthanhtoan/<int:pk>", views.HopDongThanhToanMixinsView.as_view(), name = 'hopdongthanhtoan-retrieive-delete')
]