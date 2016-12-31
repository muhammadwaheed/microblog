from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'fake'} #fake user
    posts = [{'author': {'nickname': 'Mike'},'body': 'Beautiful day'}, {'author': {'nickname': 'Choi'},'body': 'Success Reloading ...'}]
    return render_template('index.html', title='Home', user=user, posts=posts)