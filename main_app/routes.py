from flask import render_template
from main_app import app

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

