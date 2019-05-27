from django.shortcuts import render, redirect
from  django.http     import   HttpResponse
from  django.http     import   JsonResponse
# Create your views here.
from django.views.generic.base import View


class PostView(View):

    def get(self, request):


        value = request.GET
        return JsonResponse({'city': 'beijing', 'subject': 'python'})

    def post(self, request):
    

        values = request.META
        return JsonResponse({'city': 'beijing', 'subject': 'python'})
        return redirect('https://blog.csdn.net/qw943571775/article/details/81232145')



