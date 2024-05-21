from django.urls import path
from . import views


urlpatterns = [
    path('hopdongthanhtoan/', views.SearchHopdongThanhtoanListView.as_view())
]