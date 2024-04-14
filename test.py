import itertools
import hashlib
import math


def generate_words(alphabet, min_length, max_length, part_number, part_count):
    """
    Генерация слов на основе заданного алфавита.
    """
    total_words = 0
    for length in range(min_length, max_length + 1):
        total_words += len(alphabet) ** length

    words_per_worker = math.ceil(total_words / part_count)
    print(words_per_worker)
    start_index = (part_number - 1) * words_per_worker
    end_index = min(part_number * words_per_worker, total_words)

    current_index = 0
    for length in range(min_length, max_length + 1):
        for word_tuple in itertools.product(alphabet, repeat=length):
            word = ''.join(word_tuple)
            if current_index >= start_index and current_index < end_index:
                yield word
            current_index += 1
            if current_index >= end_index:
                return


def find_hashes(alphabet, min_length, max_length, target_hash, part_number, part_count):
    """
    Поиск слов с заданным хэшем в заданном диапазоне.
    """
    for word in generate_words(alphabet, min_length, max_length, part_number, part_count):
        word_hash = hashlib.md5(word.encode()).hexdigest()
        if word_hash == target_hash:
            yield word


# Пример использования:
if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    min_length = 1
    max_length = 5
    target_hash = "e2fc714c4727ee9395f324cd2e7f331f"
    part_number = 1
    part_count = 4

    found_words = list(find_hashes(alphabet, min_length, max_length, target_hash, part_number, part_count))
    print("Найденные слова с хэшем {}: {}".format(target_hash, found_words))
