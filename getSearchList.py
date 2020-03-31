import requests
from bs4 import BeautifulSoup
import re

link = "https://www.igg-games.com/"
print("iniciando...\n")
def getSearchList(search):
  req = requests.get(f'{link}?s={search}')
  soup = BeautifulSoup(req.content, 'html.parser')
  List = [] 

  for gameArticle in soup.find_all("article", class_=re.compile('post')):
    articleTitle = str(gameArticle.find("h1", class_="uk-article-title").string)
    articleLink = str(gameArticle.find("a", class_="uk-link-reset")['href'].replace("https://", "https://www."))
    articleImg = str(gameArticle.find("img", class_=re.compile('wp-post-image'))['src'].replace("https://", "https://www."))
    game = {
      "title": articleTitle,
      "link": articleLink,
      "image": articleImg,
    }
  
    List.append(game)
  return List