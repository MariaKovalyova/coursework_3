import logging

from flask import jsonify, Blueprint

from main.utils import load_post_from_sjson, return_post_by_id
from config import POST_PATH

api_blueprint = Blueprint('api_blueprint', __name__)

logger = logging.getLogger("Basic")

@api_blueprint.route('/api/posts')
def posts_all():
    logger.debug("API: Запросов всех постов")
    posts = load_post_from_sjson(POST_PATH)
    return jsonify(posts)


@api_blueprint.route("/api/posts/<int:post_id>")
def posts_one(post_id):
    logger.debug(f"API: запрошены посты юзера с ид: {post_id}")
    return jsonify(return_post_by_id(POST_PATH, post_id))
