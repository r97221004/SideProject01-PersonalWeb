import re
from flask.helpers import url_for
from PersonalWeb.models import Message, User
from PersonalWeb.forms import HelloForm, LoginForm
from PersonalWeb import app, db
from flask import render_template, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/message', methods = ['GET', 'POST'])
def message():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name = name, body = body)
        db.session.add(message)
        db.session.commit()
        flash('留言成功, 謝謝您提供的寶貴意見與經驗分享｡')
        return redirect(url_for('message'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()    
    return render_template('message.html', form = form, messages = messages)


@app.route('/message/delete/<int:message_id>', methods = ['POST'])
@login_required
def delete_message(message_id):
    message = Message.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit()
    flash('留言已經刪除')
    return redirect(url_for('message'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        user = User.query.first()

        if user:
            # 驗證用戶名和密碼
            if username == user.username and user.validate_password(password):
                login_user(user, remember) # 登入用戶
                flash('歡迎回來')
                return redirect(url_for('index'))
            flash('錯誤的使用者或密碼')
        else:
            flash('沒有此使用者')
    return render_template('login.html', form = form)  


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('成功登出')
    return redirect(url_for('index'))


@app.route('/story')
def story():
    return render_template('story.html')
    
    
