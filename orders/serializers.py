from rest_framework import serializers
from.models import *
class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Payment
        fields=['user','payment_method','amount_paid','status','created_at']
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model=Order
        fields=['user','payment','order_number','first_name','last_name','phone','email','address_line_1']

class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=OrderProduct
        fields=['user','payment','order','product']


