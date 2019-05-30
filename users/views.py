import json

from django.shortcuts import render, redirect
from  django.http     import   HttpResponse
from  django.http     import   JsonResponse
# Create your views here.
from django.views.generic.base import View
from rest_framework.mixins import ListModelMixin

from users.models import Employee
from django.shortcuts import   render
from django.template import loader
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView




class PostView(APIView):

    # 保存数据
    def post(self, request):
        # print(request.GET)
        # age = request.GET.get("age")
        # print(age)
        # # name_obj  =  Employee.objects.filter(name__contains = name)
        # name_objs  =  Employee.objects.filter(age__gte = age).values("age","name","gender")
        age = request.data
        print(age)
        # age = request.POST
        name =age["name"]
        ages =age["age"]
        gender = age["gender"]

        obj = Employee()
        obj.name =name
        obj.age = ages
        obj.gender =gender
        obj.save()

        return HttpResponse("{}数据保存成功".format(name))

    # 获取数据
    def get(self, request):

        age  = request.GET.get("name")
        name  = Employee.objects.filter(name =age).values("name","age","gender")

        if len(name) == 0:
            html_str = 'error.html'
            template = loader.get_template(html_str)
            return HttpResponse(template.render())

        template = loader.get_template('index.html')      # type: Template
        # 渲染得到字符串
        html_str = template.render(name[0])
        # 响应请求
        return HttpResponse(html_str)

# 修改数据
    def patch(self,request):
        
        gender = request.GET.get("gender")
        name = request.GET.get("name")
        try:
            d  =  Employee.objects.get(name = name )
        except Exception:
            return  HttpResponse("数据查询失败")
        d.gender = gender
        d.save()

        return HttpResponse("{}的收入成功更改为{}".format(name,gender))





