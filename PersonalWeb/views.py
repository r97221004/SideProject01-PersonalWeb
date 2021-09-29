from flask.helpers import url_for
from PersonalWeb.models import Message
from PersonalWeb.forms import HelloForm
from PersonalWeb import app, db
from flask import render_template, flash, redirect



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