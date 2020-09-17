from flask import render_template
from . import main
from ..requests import getNewsSources, getNewsArticles


@main.route('/')
def index():
    '''
    View root function that returns index page and it's data
    '''
    title = 'News Homepage'

    sources = getNewsSources('sources')

    return render_template('index.html', title=title, sources=sources)


@main.route('/news/<id>')
def news(id):
    '''
    View function that returns a news souce
    '''
    articles = getNewsArticles(id)
    
    # title = f'{articles.source.id}'
    title = 'Articles'
    
    return render_template('news.html', title = title, articles = articles)