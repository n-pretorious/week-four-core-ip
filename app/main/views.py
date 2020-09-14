from flask import render_template
from . import  main
from ..requests import getNews

@main.route('/')
def index():
  '''
  View root function that returns index page and it's data
  '''
  title = 'News Homepage'

  sources = getNews('sources') 
    
  return render_template('index.html', title = title, sources = sources)

@main.route('/hello')
def hello():
    return 'Hello, World!'
  
  
  
  
  # business = getNews('business')
  # entertainment = getNews('entertainment')
  # general = getNews('general')
  # health = getNews('health')
  # science = getNews('science')
  # sports = getNews('sports')
  # technology = getNews('technology')