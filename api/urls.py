from django.urls import path
from .views import *

urlpatterns = [
    path('customers/', CustomerDetailCreateView.as_view(), name='cutomers'),
    path('customer/<int:pk>/', CustomerDeleteEditView.as_view(), name='cutomer'),
    path('tickets/', TicketDetailCreateView.as_view(), name='tickets'),
    path('ticket/<int:pk>/', TicketDeleteEditView.as_view(), name='ticket'),
    path('reservations/', ReservationDetailCreateView.as_view(), name='create_category'),
    path('reservation/<int:pk>/', ReservationDeleteEditView.as_view(), name='reservation'),
]
