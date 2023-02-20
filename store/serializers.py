from rest_framework import serializers
from.models import *
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields=['product_name','slug','description','price','images','stock','is_available','created_date','modified_date']
class VariationSerializer(serializers.ModelSerializer):

    class Meta:
        model=Variation
        fields=['product','subject','review','rating','ip','status','','created_at','updated_at']