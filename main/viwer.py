import logging

from flask import render_template, Blueprint, request

from config import POST_PATH, UPLOAD_FOLDER_IMG, COMMENTS_PATH, BOOKMARKS_PATH  # Импорт путей из файла config
from main.utils import *
from main.bookmarks.utils import count_bookmarkered

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")  # Блупринт для главной страницы
post_blueprint = Blueprint("post_blueprint", __name__, template_folder="templates")  # Блупринт для страницы поста
search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")  # Страница поиска
user_posts_blueprint = Blueprint("user_posts_blueprint", __name__, template_folder="templates")  # Посты пользователя
post_tag_blueprint = Blueprint("post_tag_blueprint", __name__, template_folder="templates")  # Поиск по тегу

logger = logging.getLogger("basic")

""" Главная страница (лента) """
@main_blueprint.route("/")
def main_page():
    logger.debug("Запрос - главная страница")
    posts = load_post_from_sjson(POST_PATH, True)
    bookmark_count = count_bookmarkered(BOOKMARKS_PATH)  # Получаем количество сохранённых постов в закладках
    return render_template("main_page.html", posts=posts, path=UPLOAD_FOLDER_IMG, b_cout=bookmark_count)  # path - путь к файлу с картинками
"""
Решение src="{{ path }}/eye.png" почему-то работает только в первом блупринте @main_blueprint.route('/')
В остальных html-шаблонах, работающих с другими блюпринтами используется "{{ url_for('static', filename='eye.png') }}"
"""

""" Страница поста """
@post_blueprint.route("/posts/<int:post_id>")
def post_page(post_id):
    post = return_post_by_id(POST_PATH, post_id, True)  # Получаем нужный пост
    logger.debug(f"Запрос - страница post для пользователя с ид: {post_id}")
    comments = return_comment_by_postid(COMMENTS_PATH, post_id)  # И комментарии к этому посту
    return render_template("post.html", comments=comments, post=post, lencom=len(comments))

""" Страница поиска по слову """
@search_blueprint.route("/search")
def search_page():
    s = request.args.get('s', "")  # Получение ?s= аргумента из адресной строки
    logger.debug(f"Запрос - страница search для слова: {s}")
    posts = get_post_with_word(POST_PATH, s)
    postlen = len(posts)
    return render_template("search.html", posts=posts, postlen=postlen)

""" Страница постов пользователя"""
@user_posts_blueprint.route("/users/<string:username>")
def posts_by_user_page(username):
    logger.debug(f"Запрос - страница users для пользователя: {username}")
    posts = return_post_by_name(POST_PATH, username)
    return render_template("user-feed.html", posts=posts)

""" Страница поиска по тегу"""
@post_tag_blueprint.route("/tag/<string:tag>")
def posts_by_tag(tag):
    logger.debug(f"Запрос - страница tag для тега: {tag}")
    posts = get_posts_by_tag(POST_PATH, tag)
    return render_template("tag.html", posts=posts, tag=tag)