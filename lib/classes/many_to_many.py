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
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        articles = self.articles()
        
        if not articles:
            return None
        
        categories = set(article.magazine.category for article in articles)
        return list(categories)

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
        articles = [article for article in Article.all if article.magazine == self]
        
        if not articles:
            return None
        
        return [article.title for article in articles]

    def contributing_authors(self):
        articles = [article for article in Article.all if article.magazine == self]
        
        if not articles:
            return None
        
        author_counts = {}
        for article in articles:
            if isinstance(article.author, Author):
                author_counts[article.author] = author_counts.get(article.author, 0) + 1
        
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        
        return contributing_authors if contributing_authors else None