from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from category.serializers import *

@api_view(['GET'])
def category(request):
    cat_obj=Category.objects.all()
    serializer=CategorySerializer(cat_obj,many=True)
    return Response({'payload':serializer.data})



