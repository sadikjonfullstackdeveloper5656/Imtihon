from django.db import models
from django.contrib.auth.models import User


class CustomerModel(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=12)
    age = models.PositiveIntegerField()
    contact = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.fname} {self.lname}"


class TicketModel(models.Model):
    ticket_num = models.PositiveIntegerField()
    date_avail = models.DateField()
    date_flight = models.DateField()
    date_depart = models.DateTimeField()
    date_land = models.DateTimeField()
    destination = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.ticket_num}"


class ReservationModel(models.Model):
    customer_model = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(TicketModel, on_delete=models.CASCADE)
    date_res = models.DateTimeField(auto_now_add=True)
    date_acc = models.DateField()

    def __str__(self):
        return f"{self.customer_model}"
