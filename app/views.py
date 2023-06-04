from flask import render_template, redirect, url_for

from . import app, db
from .forms import NewQuery, EmailSearch
from .models import Query, User


@app.route('/')
def index():
    return render_template('index.html',
                           title='Главная')


@app.route('/history_search', methods=['GET', 'POST'])
def history_search():
    form = EmailSearch()
    queries = Query.query.all()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        queries = user.queries
        form = EmailSearch()

    queries = [{
        'query_title': 'Кроссовки',
        'discount': 22,
        'created_at': '12-10-12',
    }]
    return render_template(
        'history_search.html',
        title='История запросов',
        form=form,
        queries=queries,
    )

@app.route('/notifications', methods=['GET', 'POST'])
def notifications_page():
    form = EmailSearch()
    notifications = Query.query.all()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        notifications = user.notifications
        form = EmailSearch()

    notifications = [{
        'name': 'Кроссовки',
        'discount': 22,
        'created_at': '12-10-12',
        'notif': 'YES',
        'date_notif': '12-11-12',
        'good_id': '12',
    },
    {
        'name': 'Платья',
        'discount': "60",
        'created_at': '12-10-12',
        'notif': 'YES',
        'date_notif': '12-11-12',
        'good_id': '1200',
    }]

    return render_template('notifications.html',
                            title='Уведомления',
                            form=form,
                            notifications=notifications,
                            )

@app.route('/help')
def help_page():
    return render_template('help.html', title='Помощь')


@app.route('/add_query', methods=['GET', 'POST'])
def add_query():
    form = NewQuery()
    if form.validate_on_submit():
        user = form.user.data
        email = form.email.data
        query = form.query.data
        percent = form.percent.data
        # ToDo: сделать добавление в базу пользователя и квери
        # db.session.add(query_obj)
        # db.session.commit()
        return redirect(url_for('history_search'), email=email)
        # ToDo: редирект на history_search должен происходить с уже введенным имейлом пользователя, как это сделать?
    return render_template('add_query.html', title='Новый запрос', form=form)
