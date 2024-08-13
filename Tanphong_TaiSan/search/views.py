from rest_framework import generics

from backend.models import *
from backend.serializer import *

# Create your views here.
class SearchHopdongThanhtoanListView(generics.ListAPIView):
    queryset = ThanhtoanDichvu.objects.prefetch_related('thanhtoan')
    serializer_class = ThanhtoanDichvuSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        param_query = self.request.GET.get("id_hopdong")
        if param_query is not None:
            return queryset.search_hopdong(param_query).order_by("id")
        return None