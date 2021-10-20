from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

app = Flask('PersonalWeb')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
csrf = CSRFProtect(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    from PersonalWeb.models import User
    user = User.query.get(int(user_id))
    return user

login_manager.login_view = 'login'
# login_manager.login_message = 'Your custom message'


from PersonalWeb import views, models, forms, errors, commands

