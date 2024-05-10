import django_filters
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny

from products.models import Producer, Supplier
from products.permissions import ActiveEmployee

from products.serializers import ProducerSerializer, SupplierSerializer


class ProducerAPIView(generics.ListAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = [ActiveEmployee]


class ProducerCreateAPIView(generics.CreateAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = [AllowAny]


class ProducerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = [ActiveEmployee]


class ProducerUpdateAPIView(generics.UpdateAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = [ActiveEmployee]


class ProducerDestroyAPIView(generics.DestroyAPIView):
    queryset = Producer.objects.all()
    permission_classes = [ActiveEmployee]


class SupplierFilter(django_filters.FilterSet):
    class Meta:
        model = Supplier
        fields = ['country']


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter
    permission_classes = [ActiveEmployee]
