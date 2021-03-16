from rest_framework import generics
from rest_framework.response import Response
from django_filters import rest_framework as filters
from orders.models import Order, OrderItem
from orders.serializers import (
    OrderItemSerializer, OrderSerializer,
    OrderCreateSerializer
)
import africastalking
from decouple import config


class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        detail_serializer = OrderSerializer(order)
        return Response(detail_serializer.data)

class ListOrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('customer__id', 'status')


class RetrieveDestroyUpdateOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'id'


class CreateOrderItemView(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class RetrieveDestroyUpdateOrderItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_url_kwarg = 'id'



username = config('username')
api_key = config('api_key') 
africastalking.initialize(username, api_key)
sms = africastalking.SMS
response = sms.send("Marline we have received your order!", ["+254700921843","+254742866003"])
# print(response)
def on_finish(error, response):
    if error is not None:
        raise error
    # print(response)

sms.send("Marline we have received your order!", ["+254700921843","+254742866003"], callback=on_finish)    