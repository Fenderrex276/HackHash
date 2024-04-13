from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import Hash
from .serializers import HashSerializer
import uuid


class Crack(APIView):

    def post(self, request):
        print(request.data)
        request_id = uuid.uuid4()
        Hash.objects.create(request_id=request_id, status=Hash.Status.in_progress)
        return JsonResponse({"requestId": request_id})


class Status(APIView):

    def get(self, request):
        request_id = request.GET.get("requestId", "")
        print(request_id)
        status_id = Hash.objects.get(request_id=request_id)
        return JsonResponse({"status": status_id.status, "data": status_id.data}, status=status.HTTP_200_OK)


class Worker(APIView):
    def patch(self, request):
        pass
