from django.http.response import JsonResponse
from django.views import View

class JsonResponser(object):
    def __init__(self):
        pass

    @classmethod
    def get_response(cls, data):
        return JsonResponse(data, safe=type(data)==dict)

