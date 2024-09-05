class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        Article.all.append(self)
        self.set_title(title)

    def set_title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters.")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self.set_title(value)
    
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise TypeError("Magazine must be of type Magazine")
        
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self.set_author(value)

    def set_author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise TypeError("Author must be of type Author")
    
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))


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
        return [article for article in Article.all if article.author == self]
    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

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
            self._name = name
        else:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string.")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles() if isinstance(article.author, Author)))

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass