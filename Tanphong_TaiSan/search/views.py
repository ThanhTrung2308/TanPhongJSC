from rest_framework import generics

from backend.models import *
from backend.serializer import *

# Create your views here.
class SearchThanhToanListView(generics.ListAPIView):
    queryset = Thanhtoan.objects.all()
    serializer_class = ThanhToanSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        param_query = self.request.GET.get("hopdong")
        if param_query is not None:
            return queryset.search_hopdong(param_query)
        return None