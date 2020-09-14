from flask import Blueprint
from flask import render_template
from ..requests import getNews

try:
  from . import views,errors
except:
  pass


main = Blueprint('main', __name__)

@main.route('/')
def index():
    '''
    View root function that returns index page and it's data
    '''
    title = 'News Homepage'

    sources = getNews('sources') 
        
    return render_template('index.html', title = title, sources = sources)