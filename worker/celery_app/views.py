from billiard.exceptions import TimeLimitExceeded
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import find_hashes_task, timeout_except


# Create your views here.

class GetHash(APIView):
    def post(self, request):
        data = request.data

        find_hashes_task.delay(int(data['max_length']), data['hash'], data['request_id'])

        print(data)
        return Response(status=status.HTTP_200_OK)
