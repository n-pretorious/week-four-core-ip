import urllib.request, json
from .models import News

# Getting api key
api_key = None
# Getting the movie base url
base_url = None


def configureRequest(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def processResults(newsList):
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


def getNews(sources):
    '''
    Function that gets the json response to our url request
    
    Args:
        sources: a list of dictionaries that contains news sources
        
    Returns:
        newsResults: a list of news object
    '''

    getSourcesUrl = base_url.format(sources, api_key)

    with urllib.request.urlopen(getSourcesUrl) as Url:
        getSourcesData = Url.read()
        getSourcesResponse = json.loads(getSourcesData)

        newsResults = None

        if getSourcesResponse['sources']:
            newsResultList = getSourcesResponse['sources']
            newsResults = processResults(newsResultList)
    print(newsResults[0])
    return newsResults
