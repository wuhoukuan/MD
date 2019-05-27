from django.shortcuts import render, redirect
from  django.http     import   HttpResponse
from  django.http     import   JsonResponse
# Create your views here.
from django.views.generic.base import View


class PostView(View):

    def get(self, request):


        pass
        return JsonResponse({'city': 'beijing', 'subject': 'python'})

    def post(self, request):
        """post请求： 执行发帖操作"""
        # 代码简略

        values = request.META
        return redirect('https://blog.csdn.net/qw943571775/article/details/81232145')





        pass

