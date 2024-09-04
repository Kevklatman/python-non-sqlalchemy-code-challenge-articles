class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
        if isinstance(title, str) and 5 <= len(title) <= 50  :
            self._title = title
        else:
            raise TypeError(
                "Title must be a type of string."
            )

    @property
    def title(self):
        if hasattr(self, '_title'):
            return self._title
        else: 
            raise AttributeError("title has not been initialized")
    

        
class Author:
    all = []
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Author name must be a non-empty string.")

    @property
    def name(self):
        if hasattr(self, '_name'):
            return self._name
        else:
            raise AttributeError("Author name has not been initialized.")
        

    def articles(self):
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        Article(title, self, magazine)

    def topic_areas(self):
        pass

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name        
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name=name
        else:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and 0 < len(category):
            self._category=category
        else:
            raise ValueError("Category must be a string characters.")

    def articles(self):
        return [article.title for article in Article.all if article.magazine == self]

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass