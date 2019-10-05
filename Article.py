class Article:
    def __init__(self,title, subtitle, author, content):
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.content = content
    def display (self):
        print(self.title)
        print(self.subtitle)
        print(self.author)
        print(self.content)