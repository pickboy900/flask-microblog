from flask import render_template, flash, redirect
from main_app import app
from main_app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Maruf'}
    posts = [
            {'author': {'username': 'Jahangir'},
                'body': 'Aj shudu Ma dibos'
                },
            {
                'author': {'username': 'Jibon'},
                'body': 'Beshi porisrome shouvaggo mele.'
                }
            ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.date}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

