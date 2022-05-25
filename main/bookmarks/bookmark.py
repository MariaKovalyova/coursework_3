import logging

from flask import render_template, Blueprint, redirect

from config import BOOKMARKS_PATH, POST_PATH  # иморт адреса с файлом закладок
from main.bookmarks.utils import load_bookmark_from_sjson, save_bookmark_to_sjson # иморт функций untils из директории bookmarks
from main.utils import return_post_by_id  # функция для поиска поста по ид

bookmark_blueprint = Blueprint("bookmark_blueprint", __name__, template_folder="templates")
bookmark_add_blueprint = Blueprint("bookmark_add_blueprint", __name__, template_folder="templates")
bookmark_del_blueprint = Blueprint("bookmark_del_blueprint", __name__, template_folder="templates")

logger = logging.getLogger("basic")


@bookmark_blueprint.route("/bookmarks")
def bookmark():  # страница закладок
    logger.debug("Вход на страницу Эакладки")

    bookmark_data = load_bookmark_from_sjson(BOOKMARKS_PATH)
    added_posts = []

    for post_id in bookmark_data:
        added_posts.append(return_post_by_id(POST_PATH, post_id))

    return render_template("bookmarks.html", posts=added_posts)


@bookmark_add_blueprint.route("/bookmarks/add/<int:post_id>")
def bookmark_add(post_id):  # добавление закладки
    bookmark_data = load_bookmark_from_sjson(BOOKMARKS_PATH)
    if post_id not in bookmark_data:
        bookmark_data.append(post_id)
    save_bookmark_to_sjson(BOOKMARKS_PATH, bookmark_data)
    return redirect("/", code=302)

@bookmark_del_blueprint.route("/bookmarks/remove/<int:post_id>")
def bookmark_add(post_id):  # удаление закладки
    bookmark_data = load_bookmark_from_sjson(BOOKMARKS_PATH)
    if post_id in bookmark_data:
        bookmark_data.remove(post_id)
    save_bookmark_to_sjson(BOOKMARKS_PATH, bookmark_data)
    return redirect("/", code=302)