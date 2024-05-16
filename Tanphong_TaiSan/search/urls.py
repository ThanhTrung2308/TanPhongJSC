from django.urls import path
from . import views


urlpatterns = [
    path('thanhtoan/', views.SearchThanhToanListView.as_view())
]