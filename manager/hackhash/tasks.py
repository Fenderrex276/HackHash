import requests


def send_task(request_id: str, hash: str, max_length: int):
    print(request_id, hash, max_length)
    data = {"request_id": request_id, "hash": hash, "max_length": max_length}
    requests.post(url="http://localhost:8090/internal/api/worker/hash/crack/task/", json=data)

