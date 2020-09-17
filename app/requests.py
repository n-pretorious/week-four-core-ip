import urllib.request, json
from .models import News, Article

# Getting api key
api_key = None
# Getting the movie base url
base_url = None


def configureRequest(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def processNewsResults(newsList):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        newsList: A list of dictionaries that contain news details

    Returns :
        newsResult: A list of news objects
    '''
    newsResult = []
    for newsItem in newsList:
        id = newsItem.get('id')
        name = newsItem.get('name')
        url = newsItem.get('url')
        language = newsItem.get('language')
        country = newsItem.get('country')
        category = newsItem.get('category')
        description = newsItem.get('description')

        newsObject = News(id, name, language, description, url, category,
                          country)
        newsResult.append(newsObject)

    return newsResult


def getNewsSources(sources):
    '''
    Function that gets the json response to our url request
    
    Args:
        sources: a list of dictionaries that contains news sources
        
    Returns:
        newsResults: a list of news object
    '''

    getSourcesUrl = base_url.format(sources + '?', api_key)

    with urllib.request.urlopen(getSourcesUrl) as url:
        getSourcesData = url.read()
        getSourcesResponse = json.loads(getSourcesData)

        newsResults = None

        if getSourcesResponse['sources']:
            newsResultList = getSourcesResponse['sources']
            newsResults = processNewsResults(newsResultList)

    return newsResults


def processArticlesResults(articlesList):
    '''
    Function  that processes the news articles result and transform them to a list of Objects

    Args:
        articlesList: A list of dictionaries that contain news article details

    Returns :
        articleResult: A list of articles objects
    '''
    articleResult = []
    for articleItem in articlesList:
        source = articleItem.get('source')
        author = articleItem.get('author')
        title = articleItem.get('title')
        description = articleItem.get('description')
        url = articleItem.get('url')
        urlToImage = articleItem.get('urlToImage')
        publishedAt = articleItem.get('publishedAt')
        content = articleItem.get('content')

        articleObject = Article(source, author, title, description, url,
                                urlToImage, publishedAt, content)

        articleResult.append(articleObject)

    return articleResult


def getNewsArticles(id):
    '''
    Function that gets the json response to our url request
    
    Args:
        id: contains id for a news source
        
    Returns:
        newsArticleObject: an object for a news source
    '''
    getSourceDetailUrl = base_url.format('everything?sources=' + id + '&',
                                         api_key)

    with urllib.request.urlopen(getSourceDetailUrl) as url:
        getNewsArticleData = url.read()
        getNewsArticleResponse = json.loads(getNewsArticleData)

        newsArticleResults = None

        if getNewsArticleResponse['articles']:
            newsArticleList = getNewsArticleResponse['articles']
            newsArticleResults = processArticlesResults(newsArticleList)

    return newsArticleResults
