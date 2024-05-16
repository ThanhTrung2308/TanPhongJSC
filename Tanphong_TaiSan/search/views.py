from rest_framework import generics

from backend.models import *
from backend.serializer import *

# Create your views here.
class SearchThanhToanListView(generics.ListAPIView):
    queryset = Thanhtoan.objects.all()
    serializer_class = ThanhToanSerializer
