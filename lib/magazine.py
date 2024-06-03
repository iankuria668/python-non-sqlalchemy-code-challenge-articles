class Magazine:
    all_magazines = []

    def __init__(self,name,category):
        if not isinstance(name,str) or (2<=len(name) <= 0):
            raise ValueError('Name should be entered')
        self.name = name
        if not isinstance(category,str) or len(category) == 0:
            raise ValueError('Name should be entered')
        self.name = name
        self._category = category
    
    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
    
    def add_articles(self,article):
        self._articles.append(article)

    def articles(self):
        return self.add_articles
    
    def contributors(self):
        return list({article.author for article in self._articles})
    
    def contributing_authors(self):
        if not self._article:
            return None
        count  = {}
        for article in self._articles:
            count[article.author] = count.get(article.author, 0) + 1
            return [author for author, x in  count.items() if x > 2]
    
    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return cls._all_magazines