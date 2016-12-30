from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'fake'} #fake user
    return '''
    <html>
    <body>
    <head>
    <title>Home Page </title>
    </head>
    <h1>Hello, '''+user['username']+''' </h1>
    </body>
    </html>'''