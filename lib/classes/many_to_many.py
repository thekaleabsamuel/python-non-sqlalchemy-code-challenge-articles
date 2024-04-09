class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Can't change title")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        self._magazine = new_magazine


class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Can't change name")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set([article.magazine.category for article in self.articles()]))


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) < 2 or len(new_name) > 16:
            self._name = "Default Name"
        else:
            self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) <= 0:
            self._category = "Default Category"
        else:
            self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]

    def contributing_authors(self):
        authors = {}
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        contributing_authors = [author for author, count in authors.items() if count > 2]
        return contributing_authors if contributing_authors else None
    
    
# class Article:
#     all = []

#     def __init__(self, author, magazine, title):
#         self._author = author
#         self._magazine = magazine
#         self._title = title
#         Article.all.append(self)

#     @property
#     def title(self):
#         return self._title

#     @property
#     def author(self):
#         return self._author

#     @author.setter
#     def author(self, new_author):
#         self._author = new_author

#     @property
#     def magazine(self):
#         return self._magazine

#     @magazine.setter
#     def magazine(self, new_magazine):
#         self._magazine = new_magazine


# class Author:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     def articles(self):
#         return [article for article in Article.all if article.author == self]

#     def magazines(self):
#         return list(set([article.magazine for article in self.articles()]))

#     def add_article(self, magazine, title):
#         article = Article(self, magazine, title)
#         return article

#     def topic_areas(self):
#         if not self.articles():
#             return None
#         return list(set([magazine.category for magazine in self.magazines()]))


# class Magazine:
#     def __init__(self, name, category):
#         self._name = name
#         self._category = category

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, new_name):
#         self._name = new_name

#     @property
#     def category(self):
#         return self._category

#     @category.setter
#     def category(self, new_category):
#         self._category = new_category

#     def articles(self):
#         return [article for article in Article.all if article.magazine == self]

#     def contributors(self):
#         return list(set([article.author for article in self.articles()]))

#     def article_titles(self):
#         articles = self.articles()
#         if not articles:
#             return None
#         return [article.title for article in articles]

#     def contributing_authors(self):
#         authors = self.contributors()
#         contributing_authors = [author for author in authors if len(author.articles()) > 2]
#         if not contributing_authors:
#             return None
#         return contributing_authors

# class Article:
#     def __init__(self, author, magazine, title):
#         self._author = author
#         self._magazine = magazine
#         self._title = title

#     @property
#     def title(self):
#         return self._title

#     @property
#     def author(self):
#         return self._author

#     @author.setter
#     def author(self, new_author):
#         self._author = new_author

#     @property
#     def magazine(self):
#         return self._magazine

#     @magazine.setter
#     def magazine(self, new_magazine):
#         self._magazine = new_magazine

# class Author:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     def articles(self):
#         return [article for article in Article.all if article.author == self]

#     def magazines(self):
#         return list(set([article.magazine for article in self.articles()]))

#     def add_article(self, magazine, title):
#         article = Article(self, magazine, title)
#         return article

#     def topic_areas(self):
#         if not self.articles():
#             return None
#         return list(set([magazine.category for magazine in self.magazines()]))

# class Magazine:
#     def __init__(self, name, category):
#         self._name = name
#         self._category = category

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, new_name):
#         self._name = new_name

#     @property
#     def category(self):
#         return self._category

#     @category.setter
#     def category(self, new_category):
#         self._category = new_category

#     def articles(self):
#         return [article for article in Article.all if article.magazine == self]

#     def contributors(self):
#         return list(set([article.author for article in self.articles()]))

#     def article_titles(self):
#         articles = self.articles()
#         if not articles:
#             return None
#         return [article.title for article in articles]

#     def contributing_authors(self):
#         authors = self.contributors()
#         contributing_authors = [author for author in authors if len(author.articles()) > 2]
#         if not contributing_authors:
#             return None
#         return contributing_authors