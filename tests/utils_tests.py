""" Тест функций, которые используются в API"""

from config import POST_PATH  # Импорт адреса json файла из папки config
from main.utils import *

posts = load_post_from_sjson(f"../{POST_PATH}")

""" Тест загрузки json"""
assert type(posts) == list
assert type(posts[0]) == dict

keys_ex = {"poster_name",  # Эталонный набор ключей
           "poster_avatar",
           "pic",
           "content",
           "views_count",
           "likes_count",
           "pk"}

""" Тест наличия ключей в json файле"""
for post in posts:
    first_post_keys = set(post.keys())
    assert first_post_keys == keys_ex

