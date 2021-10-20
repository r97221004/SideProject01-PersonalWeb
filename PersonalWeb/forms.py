from flask_wtf import FlaskForm
from wtforms.fields.core import BooleanField, StringField
from wtforms.fields.simple import PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length



class HelloForm(FlaskForm):
    name = StringField(label = '姓名', validators = [DataRequired(), Length(1, 20)], render_kw = {'placeholder': '大古翔平'})
    body = TextAreaField(label = '內文', validators=[DataRequired(), Length(1, 200)], render_kw = {'placeholder': '我很確定我以後一定會遇到一面阻擋自己的牆, 一旦我撞上這面牆, 那我就得更加努力去嘗試, 付出一切去跨越這道牆｡'} )
    submit = SubmitField(label='決定送出')

class LoginForm(FlaskForm):
    username = StringField(label = '', validators=[DataRequired(), Length(1, 20)], render_kw = {'placeholder': '使用者帳號'})
    password = PasswordField(label= '', validators = [DataRequired(), Length(1, 128)], render_kw = {'placeholder': '使用者密碼'})
    submit = SubmitField(label = '登入')
    remember = BooleanField(label = '記住我')
    