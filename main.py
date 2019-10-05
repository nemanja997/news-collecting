import requests
from bs4 import BeautifulSoup
from Article import Article

def isTextArticleFilter(article):
    if('video-article' in article['href']):
        return False
    else:
        return True

r1 = requests.get('https://techcrunch.com/')
firstPage = r1.content
articles = []
articlesTitles = []
articleURLs = []

soup = BeautifulSoup(firstPage, 'html.parser')

articlesTitles = filter(isTextArticleFilter,soup.find_all('a', class_='post-block__title__link'))
articleURLs = map(lambda x: x.get('href'), articlesTitles)

for url in articleURLs:
    articlePage = requests.get(url).content
    soupArticle = BeautifulSoup(articlePage, 'html.parser')
    title = soupArticle.find('h1', class_='article__title').get_text()
    # subtitle = soupArticle.find('h2',class_='article__subtitle').get_text()
    author = soupArticle.find('div',class_='article__byline').find('a').get_text().strip()
    content = soupArticle.find('div',class_='article-content').get_text()

    article = Article(title, "blank", author, content)
    articles.append(article)

articles[0].display()



