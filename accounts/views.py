from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from accounts.models import Customer, Staff
from accounts.serializers import CustomerSerializer,StaffSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAssigned


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated, ]



    def list(self, request):
        queryset = Staff.objects.all()
        serializer = StaffSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Staff.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = StaffSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        new_staff = StaffSerializer(data=request.data)
        if new_staff.is_valid():
            new_staff.save()
            return Response(new_staff.data, status=201)
        return Response(new_staff.errors, status=400)




class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [BasicAuthentication, ]
    permission_classes = [IsAuthenticated, ]



    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Customer.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        new_customer = CustomerSerializer(data=request.data)
        if new_customer.is_valid():
            new_customer.save()
            return Response(new_customer.data, status=201)
        return Response(new_customer.errors, status=400)