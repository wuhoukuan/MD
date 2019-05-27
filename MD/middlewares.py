from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None):
        super().__init__(get_response)
        print('init')

    def process_request(self, request):
        print('before 视图')
        # 注意：可以返回None或者response对象，如果返回response对象，则视图函数就不会再执行了

    def process_response(self, request, response):
        print('after 视图')
        return response