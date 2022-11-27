from rest_framework import viewsets
from rest_framework import mixins

from .filters import GoodsFilter
from .models import Goods
from .serializers import GoodsSerializer

from django_filters import rest_framework
from rest_framework.filters import SearchFilter, OrderingFilter


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    列出所有的Goods。
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ['name']
    ordering_fields = ('shop_price', 'name')
