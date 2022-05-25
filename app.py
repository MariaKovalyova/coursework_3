from flask import Flask

from main.viwer import main_blueprint, post_blueprint, search_blueprint, user_posts_blueprint, \
                        post_tag_blueprint  # импорт блюпринтов
from main.errors.errors import blueprint_errors  # импорт блюпринтов c ошибками
from main.API.viwes import api_blueprint  # Api
from main.bookmarks.bookmark import bookmark_blueprint, bookmark_add_blueprint, bookmark_del_blueprint # закладки
from logger import create_logger  # импорт функции создания логгера

app = Flask(__name__)

create_logger()  # Создание лог-файла

""" main. viwer"""
app.register_blueprint(main_blueprint)  # Блюпринт ленты
app.register_blueprint(post_blueprint)  # Блюпринт страницы с постом
app.register_blueprint(search_blueprint)  # Блюпринт страницы поиска
app.register_blueprint(user_posts_blueprint)  # Блюпринт страницы постов пользователя
app.register_blueprint(post_tag_blueprint)  # Блюпринт страницы тэгов
""" main.errors.errors """
app.register_blueprint(blueprint_errors)  # Блюпринт для обработки ошибок
""" main.api.viwes """
app.register_blueprint(api_blueprint)  # Api
""" main.bookmarks.bookmark"""
app.register_blueprint(bookmark_blueprint)  # Блюпринт страницы закладоr
app.register_blueprint(bookmark_add_blueprint)  # Добавить закладку
app.register_blueprint(bookmark_del_blueprint)  # Удалить закладку

if __name__ == "__main__":
    """ 127.0.0.1:5000 - дефолтный IP-адрес """
    app.run(debug=False)

