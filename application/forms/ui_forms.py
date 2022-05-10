from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import Optional
from flask_babel import lazy_gettext


class LoginForm(FlaskForm):
    key = StringField("", render_kw={'rows': 5, 'cols': 5,
                                     'style': 'position:absolute;resize:None;top:50px;left:480px;'
                                              'width:150px;background-color:#C7D0CC;color:black',
                                     'placeholder': lazy_gettext('Секретный ключ')})

    title1 = StringField('', validators=[Optional()],
                         render_kw={'rows': 25, 'cols': 15,
                                    'style': 'position:absolute;resize:None;top:2px;left:0px;'
                                             'width:455px;color:black;background-color:#C7D0CC',
                                    'readonly': True},
                         default="Входной текст")

    redactor1 = TextAreaField('', validators=[Optional()],
                              render_kw={'rows': 25, 'cols': 15,
                                         'style': 'position:absolute;resize:None;top:50px;left:0px;'
                                                  'width:455px;background-color:#AEE5D6;color:black'},
                              default="Введите исходный текст")

    clear1 = SubmitField(lazy_gettext('Очистить форму'),
                         render_kw={'rows': 5, 'cols': 5,
                                    'style': 'position:absolute;resize:None;top:580px;left:0px;'
                                             'width:455px;background-color:#C7D0CC;color:black'})

    splash = SubmitField(lazy_gettext('↔️'),
                         render_kw={'rows': 5, 'cols': 5,
                                    'style': 'position:absolute;resize:None;top:2px;left:480px;'
                                             'width:150px;background-color:#C7D0CC;color:black'})

    encrypt = SubmitField(lazy_gettext('Зашифровать'),
                          render_kw={'rows': 5, 'cols': 5,
                                     'style': 'position:absolute;resize:None;top:100px;left:480px;'
                                              'width:150px;background-color:#C7D0CC;color:black'})

    decrypt = SubmitField(lazy_gettext('Расшифровать'),
                          render_kw={'rows': 5, 'cols': 5,
                                     'style': 'position:absolute;resize:None;top:150px;left:480px;'
                                              'width:150px;background-color:#C7D0CC;color:black'})

    vzlom = SubmitField(lazy_gettext('Взлом'),
                          render_kw={'rows': 5, 'cols': 5,
                                     'style': 'position:absolute;resize:None;top:200px;left:480px;'
                                              'width:150px;background-color:#C7D0CC;color:black'})

    title2 = StringField('', validators=[Optional()],
                         render_kw={'rows': 25, 'cols': 15,
                                    'style': 'position:absolute;resize:None;top:2px;left:650px;'
                                             'width:455px;color:black;background-color:#C7D0CC',
                                    'readonly': True},
                         default="Результат")

    redactor2 = TextAreaField('', validators=[Optional()],
                              render_kw={'rows': 25, 'cols': 15,
                                         'style': 'position:absolute;resize:None;top:50px;left:650px;'
                                                  'width:455px;background-color:#AEE5D6;color:black',
                                         'readonly': True},
                              default="Преобразованный текст")

    clear2 = SubmitField(lazy_gettext('Очистить форму'),
                         render_kw={'rows': 5, 'cols': 5,
                                    'style': 'position:absolute;resize:None;top:580px;left:650px'
                                             ';width:455px;background-color:#C7D0CC;color:black'})
