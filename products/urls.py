from django.urls import path
from rest_framework.routers import DefaultRouter
from products.views import (
    ProducerAPIView,
    ProducerRetrieveAPIView,
    ProducerCreateAPIView,
    ProducerUpdateAPIView,
    ProducerDestroyAPIView,
    SupplierViewSet,
)

app_name = 'products'

router = DefaultRouter()
router.register(r'supplier', SupplierViewSet, basename='supplier')

urlpatterns = [
                  path('producer/', ProducerAPIView.as_view(), name='producers_list'),
                  path('producer/<int:pk>/', ProducerRetrieveAPIView.as_view(), name='producer_detail'),
                  path('producer/create/', ProducerCreateAPIView.as_view(), name='producer_create'),
                  path('producer/update/<int:pk>/', ProducerUpdateAPIView.as_view(), name='producer_update'),
                  path('producer/delete/<int:pk>/', ProducerDestroyAPIView.as_view(), name='producer_delete'),
              ] + router.urls
