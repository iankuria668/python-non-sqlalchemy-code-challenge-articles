class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError('Name should be a string between 2 and 16 characters')
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError('Category should be a non-empty string')
        
        self._name = name
        self._category = category
        self._articles = []

        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string")

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def contributing_authors(self):
        if not self._articles:
            return None
        count = {}
        for article in self._articles:
            count[article.author] = count.get(article.author, 0) + 1
        return [author for author, num in count.items() if num > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        return max(cls.all_magazines, key=lambda magazine: len(magazine.articles()))

