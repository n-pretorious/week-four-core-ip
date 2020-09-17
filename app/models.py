class News:
    '''
    News class to define News Objects
    '''
    def __init__(self, id, name, description, url, category, language,
                 country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language


class Article:
    '''
    Article class to define Article Object
    '''
    def __init__(self, source, author, title, description, url, urlToImage, publishedAt, content):
      self.source = source
      self.author = author
      self.title = title
      self.description = description
      self.url = url
      self.urlToImate = urlToImage
      self.publishedAt = publishedAt
      self.content = content