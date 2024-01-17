from http import HTTPStatus

from flask import flash, redirect, render_template

from yacut import app, db
from yacut.forms import URLMapForm
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


def save_url_map(form, custom_id):
    """
    Add and save an entry in the URLMap.
    """
    if not custom_id:
        custom_id = get_unique_short_id()
    url_map = URLMap(
        original=form.original_link.data,
        short=custom_id
    )
    db.session.add(url_map)
    db.session.commit()
    return custom_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """
    Creates a new short link.
    """
    form = URLMapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if URLMap.query.filter_by(short=custom_id).first():
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('yacut.html', form=form)
        short_id = save_url_map(form, custom_id)
        return render_template('yacut.html', form=form, short=short_id), HTTPStatus.OK
    return render_template('yacut.html', form=form)


@app.route('/<string:short>')
def redirect_view(short):
    """
    Redirects from a short link to a long one.
    """
    original_url = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(original_url.original)
