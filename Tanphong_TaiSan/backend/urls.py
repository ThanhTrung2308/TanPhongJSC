from django.urls import path

from . import views

urlpatterns = [
    path('hopdong/',views.HopDongAPIView.as_view()),
    path('dichvu/',views.DichVuAPIView.as_view()),
]
