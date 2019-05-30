from django.contrib.auth import login
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
# Create your views here.
from   booktest.serializers   import   BookInfoSerializer
from  booktest.models  import  BookInfo

# queryset 指明该视图集在查询数据时使用的查询集

#
#
# data =  {    }
# book = BookInfo.objects.get(id=1)
# b=  BookInfoSerializer(data=data)
# b.is_valid(True)


