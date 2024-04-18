import requests
from django.conf import settings

def send_task(request_id: str, hash: str, max_length: int):
    # print(request_id, hash, max_length)
    data = {"request_id": request_id, "hash": hash, "max_length": max_length}
    try:
        requests.post(url=f"http://{settings.WORKER_HOST}:8090/internal/api/worker/hash/crack/task/", json=data)
    except requests.exceptions.RequestException as e:
        raise Exception(e)
