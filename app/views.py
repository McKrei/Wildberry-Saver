from flask import render_template, redirect, url_for

from . import app, db
from .forms import NewQuery, EmailSearch
from .models import Query, User, Notification
from .parsing import run_task
from .crud import add_query_to_database, get_notifications

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
        if user:
            queries = user.queries
            form = EmailSearch()
    return render_template(
        'history_search.html',
        title='История запросов',
        form=form,
        queries=queries,
    )


@app.route('/notifications', methods=['GET', 'POST'])
def notifications_page():
    form = EmailSearch()
    notifications = get_notifications()
    if form.validate_on_submit():
        email = form.email.data
        notifications = get_notifications(email)
        form = EmailSearch()
    return render_template('notifications.html',
                            title='Уведомления',
                            form=form,
                            notifications=notifications,)


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
        add_query_to_database(user, email, query, percent)
        return redirect(url_for('history_search'))
    return render_template('add_query.html', title='Новый запрос', form=form)


@app.route('/get_new_data')
def get_new_data():
    run_task()
    return 'OK!'
