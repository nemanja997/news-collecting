import requests
from bs4 import BeautifulSoup
from Article import Article
import pymongo


def isTextArticleFilter(article):
    if ('video-article' in article['href']):
        return False
    else:
        return True


def getArticlesFromWebpage():
    r1 = requests.get('https://techcrunch.com/')
    soup = BeautifulSoup(r1.content, 'html.parser')
    listArticles = []


    articlesTitlesTags = filter(isTextArticleFilter, soup.find_all('a', class_='post-block__title__link'))
    articleURLs = map(lambda x: x.get('href'), articlesTitlesTags)

    for url in articleURLs:
        articlePage = requests.get(url).content
        soupArticle = BeautifulSoup(articlePage, 'html.parser')
        title = soupArticle.find('h1', class_='article__title').get_text()
        author = soupArticle.find('div', class_='article__byline').find('a').get_text().strip()
        content = soupArticle.find('div', class_='article-content').get_text()
        dictArticle = {'title': title, 'author': author, 'content': content}
        listArticles.append(dictArticle)

    return listArticles


# konekcija ka MongoDB bazi - ako ne postoji napravice novi, ali tek kada se insertuje nesto
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
# inicijalizovanje kollekcije - jos nije napravljena dok se ne insertuje nesto!
mycol = mydb["articles"]

# articles = getArticlesFromWebpage()
#
# for article in articles:
#     if(mycol.count_documents({ 'title': article['title'] }, limit = 1) == 0):
#         mycol.insert_one(article)


for x in mycol.find():
    print(x)

print(mycol.count_documents({}))