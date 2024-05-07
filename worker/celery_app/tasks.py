import itertools
import hashlib
import math
import requests
from celery import shared_task
from celery.schedules import crontab
#TODO сделать периодическую таску
from django.conf import settings
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
min_length = 1


def generate_words(alphabet, min_length, max_length):

    total_words = 0
    for length in range(min_length, max_length + 1):
        total_words += len(alphabet) ** length
    # print(total_words)

    current_index = 0
    for length in range(min_length, max_length + 1):
        for word_tuple in itertools.product(alphabet, repeat=length):
            word = ''.join(word_tuple)
            yield word
            current_index += 1
            if current_index >= total_words:
                return


@shared_task()
def find_hashes_task(max_length, target_hash, request_id):
    """
    Поиск слов с заданным хэшем в заданном диапазоне.
    """
    for word in generate_words(alphabet, min_length, max_length):
        word_hash = hashlib.md5(word.encode()).hexdigest()
        if word_hash == target_hash:
            print(word, "FINISH")
            send_result.delay(word, request_id)


# def task_bruteforce_hash(max_length, target_hash):
#     min_length = 1
#     current_word = find_hashestask(alphabet=alphabet, min_length=min_length, max_length=max_length, target_hash=target_hash)
#
#     return str(current_word)

@shared_task()
def send_result(current_word, request_id):
    data = {"current_word": str(current_word), "request_id": request_id}
    req = requests.patch(url=f"http://{settings.MANAGER_HOST}:8000/internal/api/manager/hash/crack/request/", json=data)
    print(req)


@shared_task()
def timeout_except(request_id):
    data = {"request_id": request_id}
    req = requests.patch(url=f"http://{settings.MANAGER_HOST}:8000/internal/api/manager/hash/crack/request/", json=data)
    print(req)

# Пример использования:
# if __name__ == "__main__":
#
#     min_length = 1
#     max_length = 2
#     target_hash = "d6cbb48444bf8cf4e6460eebceaefce1"
#     part_number = 4
#     part_count = 4
#
#     found_words = list(find_hashes(alphabet, min_length, max_length, target_hash, part_number, part_count))
#     print("Найденные слова с хэшем {}: {}".format(target_hash, found_words))
