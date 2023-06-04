from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired, Length, Optional, Email


class NewQuery(FlaskForm):
    user = StringField(
        'Имя пользователя',
        validators=[DataRequired(message="Поле не должно быть пустым"),
                    Length(max=10, message='Введите заголовок длиной до 10 символов')]
    )

    email = StringField(
        'Email для уведомления',
        validators=[Email(message='Введите email'), Length(max=30, message='Введите email длиной до 30 символов')]
    )

    query = StringField(
        'Введите название товара',
        validators=[DataRequired(message="Поле не должно быть пустым"),
                    Length(max=255, message='Введите заголовок длиной до 255 символов')]
    )

    percent = StringField(
        'Введите желаемую скидку, в %',
        validators=[DataRequired(message="Поле не должно быть пустым"),
                    Length(max=2, message='От 0 до 99, без %')]
    )
    submit = SubmitField('Добавить запрос')


class EmailSearch(FlaskForm):
    email = EmailField(
        'Введите email',
        validators=[Email(message='Введите email'), Length(max=30, message='Введите Емаил длиной до 30 символов')]
    )
    submit = SubmitField('Поиск')
