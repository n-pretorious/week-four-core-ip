class News:
    '''
    News class to define News Objects
    '''
    def __init__(self, id, name, category, description, url, language,
                 country):
        self.id = id
        self.name = name
        self.url = url
        self.description = description
        self.language = language
        self.category = category


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
      self.urlToImage = urlToImage
      self.publishedAt = publishedAt
      self.content = content
      