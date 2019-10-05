class Article:
    def __init__(self,title, author, content):
        self.title = title
        self.author = author
        self.content = content
    def display (self):
        print(self.title)
        print(self.author)
        print(self.content)