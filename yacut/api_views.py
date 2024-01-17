import re
from http import HTTPStatus

from flask import jsonify, request

from yacut import app, db
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.utils import get_unique_short_id

REGEX = '^[A-Za-z0-9]*$'


@app.route('/api/id/', methods=['POST'])
def add_link():
    """
    Creates a new short link.
    """
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    short_id = data.get('custom_id') or get_unique_short_id()
    if len(short_id) > 16 or not re.match(REGEX, short_id):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if URLMap.query.filter_by(short=short_id).first():
        raise InvalidAPIUsage('Предложенный вариант короткой ссылки уже существует.')
    url_map = URLMap(original=data['url'], short=short_id)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_original_url(short):
    """
    Validates the data when creating a short link.
    """
    original_url = URLMap.query.filter_by(short=short).first()
    if not original_url:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': original_url.original}), HTTPStatus.OK
