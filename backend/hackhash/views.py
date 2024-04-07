from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
import uuid


class Crack(APIView):

    def post(self, request):
        print(request.data)
        request_id = uuid.uuid4()

        return JsonResponse({"requestId": request_id})


class Status(APIView):

    def post(self, request, requestId):
        pass
