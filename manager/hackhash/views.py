from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Hash
from .serializers import HashSerializer
import uuid
from .tasks import send_task

class Crack(APIView):

    def post(self, request):
        data = request.data
        print(request.data)
        hash_data = data["hash"]
        max_length = int(data["maxLength"], 0)
        request_id = uuid.uuid4()
        send_task(request_id=str(request_id), hash=hash_data, max_length=max_length)

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
        data = request.data
        print(data)
        result = Hash.objects.get(request_id=data['request_id'])
        result.data = data['current_word']
        result.status = Hash.Status.ready
        result.save()
        return Response(status=status.HTTP_200_OK)

