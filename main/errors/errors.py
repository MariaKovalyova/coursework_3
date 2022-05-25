from flask import Blueprint

blueprint_errors = Blueprint('errors', __name__)


@blueprint_errors.app_errorhandler(404)  # Ошибка, если страницы не существует
def error_404(error):
    return '<h1> Ошибка 404. Запрашиваемой страницы не существует <h1> \
           <h3><a href="/">Вернуться на главную страницу</a></h3>', 404


@blueprint_errors.app_errorhandler(500)  # Ошибка, если что-то сломалось
def error_500(error):
    return '<h1>Internal Server Error</h1> \
<h2>The server encountered an internal error and was unable to complete your request. \
Either the server is overloaded or there is an error in the application.</h2> \
    <h3><a href="/">Вернуться на главную страницу</a></h3>', 500