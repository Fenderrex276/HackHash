from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.cache import cache
from .models import Hash
from django.conf import settings
from .serializers import HashSerializer
import uuid
from .tasks import send_task

class Crack(APIView):

    def post(self, request):
        data = request.data
        hash_data = data["hash"]
        max_length = int(data["maxLength"], 0)
        if hash_data is None or max_length == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        request_id = uuid.uuid4()
        cache.set(str(request_id), Hash.Status.in_progress, settings.CACHE_TIMEOUT)
        cache.set(f"{str(request_id)} data", None, settings.CACHE_TIMEOUT)
        send_task(request_id=str(request_id), hash=hash_data, max_length=max_length)

        return JsonResponse({"requestId": request_id})


class Status(APIView):

    def get(self, request):
        request_id = request.GET.get("requestId", "")
        if request_id == "":
            return Response(status=status.HTTP_404_NOT_FOUND)
        # print(request_id)
        status_id = cache.get(request_id)
        data = cache.get(f"{str(request_id)} data")
        # print("ITS CACHE", data)
        # print(cache.get(f"{str(request_id)} data"))

        return JsonResponse({"status": status_id, "data": data}, status=status.HTTP_200_OK)


class Worker(APIView):
    def patch(self, request):
        data = request.data
        print(data)
        request_id = data['request_id']
        word = data['current_word']

        cache.set(request_id, Hash.Status.ready, settings.CACHE_TIMEOUT)
        cache.set(f'{request_id} data', word, settings.CACHE_TIMEOUT)
        return Response(status=status.HTTP_200_OK)

