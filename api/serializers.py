from rest_framework import serializers
from api.models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = "__all__"
        read_only_fields = ('id',)

    def create(self, validated_data):
        return CustomerModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.fname = validated_data.get('fname', instance.fname)
        instance.lname = validated_data.get('lname', instance.lname)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.age = validated_data.get('age', instance.age)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketModel
        fields = "__all__"
        read_only_fields = ('id',)

    def create(self, validated_data):
        return TicketModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ticket_num = validated_data.get('ticket_num', instance.ticket_num)
        instance.date_avail = validated_data.get('date_avail', instance.date_avail)
        instance.date_flight = validated_data.get('date_flight', instance.date_flight)
        instance.date_depart = validated_data.get('date_depart', instance.date_depart)
        instance.date_land = validated_data.get('date_land', instance.date_land)
        instance.destination = validated_data.get('destination', instance.destination)
        return instance


class ReadOnlyReservationSerializer(serializers.ModelSerializer):
    customer_model = CustomerSerializer()
    ticket = TicketSerializer()
    admin = serializers.SerializerMethodField()

    class Meta:
        model = ReservationModel
        fields = "__all__"
        read_only_fields = ('id',)

    def get_admin(self, obj):
        user = obj.admin
        admin_data = {
            'id': user.id,
            'name': user.username,
            'email': user.email
        }
        return admin_data


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationModel
        fields = "__all__"
        read_only_fields = ('id',)

    def create(self, validated_data):
        return ReservationModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.customer_model = validated_data.get('customer_model', instance.customer_model)
        instance.admin = validated_data.get('admin', instance.admin)
        instance.ticket = validated_data.get('ticket', instance.ticket)
        instance.date_res = validated_data.get('date_res', instance.date_res)
        instance.date_acc = validated_data.get('date_acc', instance.date_acc)
        instance.save()
        return instance
