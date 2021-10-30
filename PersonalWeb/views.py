from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from PersonalWeb import app, db
from PersonalWeb.models import Message, Story, User
from PersonalWeb.forms import HelloForm, LoginForm, PostForm


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


@app.route('/story', methods = ['GET', 'POST'])
def story():
    stories = Story.query.all()
    form = PostForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            return redirect(url_for('index'))
        title = form.title.data
        body = form.body.data
        site = form.site.data
        story = Story(title = title, body = body, site = site)
        db.session.add(story)
        db.session.commit()
        flash('新增最新動態')
        return redirect(url_for('story'))
    return render_template('story.html', stories = stories, form = form)


@app.route('/story/edit/<int:story_id>', methods = ['GET', 'POST'])
@login_required
def edit_story(story_id):
    form = PostForm()
    story = Story.query.get_or_404(story_id)
    if form.validate_on_submit():
        story.title = form.title.data
        story.body = form.body.data
        story.site = form.site.data
        db.session.commit()
        flash('更新成功')
        return redirect(url_for('story'))
    form.title.data = story.title
    form.body.data = story.body
    form.site.data = story.site
    return render_template('edit_story.html', form = form)


@app.route('/story/delete/<int:story_id>', methods = ['POST'])
@login_required
def delete_story(story_id):
    story = Story.query.get_or_404(story_id)
    db.session.delete(story)
    db.session.commit()
    flash('動態已經刪除')
    return redirect(url_for('story'))


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



    
    
