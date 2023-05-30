from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView


class CustomerDetailCreateView(GenericAPIView):
    serializer_class = CustomerSerializer
    queryset = CustomerModel.objects.all()

    def post(self, request):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        serializer = self.get_serializer_class()(CustomerModel.objects.all(), many=True)
        return Response(data=serializer.data)


class CustomerDeleteEditView(GenericAPIView):
    lookup_field = 'pk'
    serializer_class = CustomerSerializer
    queryset = CustomerModel.objects.all()

    def get(self, request, pk):
        category = get_object_or_404(CustomerModel, pk=pk)
        serializer = self.get_serializer_class()(category)
        return Response(data=serializer.data)

    def patch(self, request, pk):
        category = get_object_or_404(CustomerModel, pk=pk)
        serializer = self.get_serializer_class()(category, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(category, serializer.validated_data)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        category = get_object_or_404(CustomerModel, pk=pk)
        serializer = self.get_serializer_class()(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(category, serializer.validated_data)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk):
        category = get_object_or_404(CustomerModel, pk=pk)
        category.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)


class ReservationDetailCreateView(GenericAPIView):
    serializer_class = ReservationSerializer
    queryset = ReservationModel.objects.all()

    def post(self, request):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        serializer = ReadOnlyReservationSerializer(ReservationModel.objects.all(), many=True)
        return Response(data=serializer.data)


class ReservationDeleteEditView(GenericAPIView):
    lookup_field = 'pk'
    serializer_class = ReservationSerializer
    queryset = ReservationModel.objects.all()

    def get(self, request, pk):
        category = get_object_or_404(ReservationModel, pk=pk)
        serializer = ReadOnlyReservationSerializer(category)
        return Response(data=serializer.data)

    def patch(self, request, pk):
        category = get_object_or_404(ReservationModel, pk=pk)
        serializer = self.get_serializer_class()(category, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(category, serializer.validated_data)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        category = get_object_or_404(ReservationModel, pk=pk)
        serializer = self.get_serializer_class()(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(category, serializer.validated_data)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk):
        category = get_object_or_404(ReservationModel, pk=pk)
        category.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)


class TicketDetailCreateView(GenericAPIView):
    serializer_class = TicketSerializer
    queryset = TicketModel.objects.all()

    def post(self, request):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        serializer = self.get_serializer_class()(TicketModel.objects.all(), many=True)
        return Response(data=serializer.data)


class TicketDeleteEditView(GenericAPIView):
    lookup_field = 'pk'
    serializer_class = TicketSerializer
    queryset = TicketModel.objects.all()

    def get(self, request, pk):
        category = get_object_or_404(TicketModel, pk=pk)
        serializer = self.get_serializer_class()(category)
        return Response(data=serializer.data)

    def patch(self, request, pk):
        category = get_object_or_404(TicketModel, pk=pk)
        serializer = self.get_serializer_class()(category, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(category, serializer.validated_data)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        category = get_object_or_404(TicketModel, pk=pk)
        serializer = self.get_serializer_class()(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(category, serializer.validated_data)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk):
        category = get_object_or_404(TicketModel, pk=pk)
        category.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)
