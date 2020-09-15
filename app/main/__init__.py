from flask import Blueprint
main = Blueprint('main', __name__)
from flask import render_template
from ..requests import getNews

try:
    from . import views
except:
    pass

# @main.route('/')
# def index():
#     '''
#     View root function that returns index page and it's data
#     '''
#     title = 'News Homepage'

#     sources = getNews('sources')

#     return render_template('index.html', title = title, sources = sources)

# @main.route('/hello')
# def hello():
#     return 'Hello, World!'