import re  # фунция для удаления знаков препинания и замены хэштэгов на ссылки

from json import load  # Импорт билиотеки для загрузки файла

from main.work_hashtag import content_edit_hashtag_links, return_first_tag  # Импорт функции работы с хэштэгами

""" При allow_add_ftag=True к словарю постов добавляется дополнительная пара ключ/значение - tag
    За главный тег, который виден в начале поста, решено принять первый тег, который
    встретится в тексте поста
"""
def load_post_from_sjson(path, allow_add_ftag=False):  # Функция загрузки файла json, получение всех постов
    with open(path, 'r', encoding="UTF=8") as file:
        posts = load(file)
    if allow_add_ftag:
        for post in posts:
            post["tag"] = return_first_tag(post.get("content"))
    return posts


def return_post_by_id(path, post_id, formtag=False):  # Функция возврата поста по его номеру. Formtag - флаг формат.
    posts = load_post_from_sjson(path)
    for post in posts:
        if post.get("pk") == post_id:
            if formtag:
                post["content"] = content_edit_hashtag_links(post.get('content'))  # Делаем хэштэги кликабельными
            return post


def return_post_by_name(path, name):  # Функция получения постов пользователя
    posts = load_post_from_sjson(path, True)
    posts_by_name_list = []  # список подходящих постов
    for post in posts:
        if post.get("poster_name") == name:
            posts_by_name_list.append(post)
    return posts_by_name_list


def return_comment_by_postid(path, post_id):  # Функция возврата поста по его номеру
    comments = load_post_from_sjson(path)
    comments_by_id_list = []
    for comment in comments:
        if comment.get("post_id") == post_id:
            comments_by_id_list.append(comment)
    return comments_by_id_list


def get_post_with_word(posts_path, word):  # Функция для поиска постов с вхождением слова
    post_list = []  # список подходящих постов
    posts = load_post_from_sjson(posts_path, True)
    for post in posts:
        if word.lower() in (re.sub(r'[^\w\s]', '', post.get('content'))).lower().split():
            post_list.append(post)
    return post_list


def get_posts_by_tag(path, tag):  # Функция для поиска постов с вхождением слова
    posts = load_post_from_sjson(path, True)
    post_with_tag_list = []
    for post in posts:
        if re.sub(r'[^\w\s]', '', post.get('tag')) == tag:
            post_with_tag_list.append(post)
    return post_with_tag_list


