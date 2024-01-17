from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    """
    A form class that works with the URLMap model.
    """
    original_link = URLField('Длинная ссылка',
                             validators=[DataRequired(message='Обязательное поле.'),
                                         Length(1, 128)])
    custom_id = StringField('Ваша короткая ссылка', validators=[Length(1, 16), Optional()])
    submit = SubmitField('Создать')
