import newspaper
from newspaper import Article
import random

websites = ['http://qz.com', 'http://www.cnn.com', 'https://www.ndtv.com/', 'https://www.nytimes.com/', 'https://www.nbcnews.com/', 'https://www.foxnews.com/', 'https://www.theguardian.com/international'] 
ch = random.choice(websites[:])
paper = newspaper.build(ch)

URL = []

keywords = 'corona'

for article in paper.articles:
    URL.append(article.url)
    print(article.url)
print(len(URL))

key_URL = []

for link in URL:
    if keywords in link:
        continue
    else:
        key_URL.append(link)
print(len(URL))


stories = []
print(len(key_URL))
key_URL =key_URL[:10]
for  i in range(len(key_URL)):
    article = Article(key_URL[i], language='en')
    article.download()
    article.parse()
    stories.append(article.text)

print(stories[0])