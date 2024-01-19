from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from yacut.variables import REGEX


class URLMapForm(FlaskForm):
    """
    A form class that works with the URLMap model.
    """
    original_link = URLField('Длинная ссылка',
                             validators=[DataRequired(message='Обязательное поле.'),
                                         Length(max=128)])
    custom_id = StringField('Ваша короткая ссылка',
                            validators=[Length(max=16), Optional(),
                                        Regexp(REGEX, message='Некорректная короткая ссылка.')])
    submit = SubmitField('Создать')
