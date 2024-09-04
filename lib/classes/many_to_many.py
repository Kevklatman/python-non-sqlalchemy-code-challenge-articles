class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
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
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    
    def __init__(self, name, category):
        self.name = name        
        self.category = category

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
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass