from json import load, dump

def load_bookmark_from_sjson(path):  # Функция загрузки файла json, получение всех постов
    with open(path, 'r', encoding="UTF=8") as file:
        return load(file)

def save_bookmark_to_sjson(path, data):
    with open(path, 'w', encoding="UTF=8") as file:
        dump(data, file)

def count_bookmarkered(path):  # Возвращает количество постов, добавленных в закладки
    return len(load_bookmark_from_sjson(path))