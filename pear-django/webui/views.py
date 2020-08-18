from rest_framework import viewsets
from crawl.models import *
from webui.serializer import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework_extensions.cache.mixins import CacheResponseMixin  # 缓存处理
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class StandardPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'pageSize'
    page_query_param = 'currPage'
    max_page_size = 20


class StarViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = Star.objects.order_by("sort").all()
    filter_backends = [OrderingFilter]
    serializer_class = starSerializer
    pagination_class = StandardPageNumberPagination
    throttle_classes = (AnonRateThrottle, UserRateThrottle)


class MovieViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = Movie.objects.order_by('-score').all()
    serializer_class = movieSerializer
    throttle_classes = (AnonRateThrottle, UserRateThrottle)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['star', 'id']


class PhotoViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = photoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['video']
    throttle_classes = (AnonRateThrottle, UserRateThrottle)


class SourceViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = sourceSerializer
    throttle_classes = (AnonRateThrottle, UserRateThrottle)
