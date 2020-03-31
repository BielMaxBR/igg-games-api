import requests
from bs4 import BeautifulSoup
import re
from getSearchList import getSearchList


def getLinkList(game):
  req = requests.get(f'{game}')
  soup = BeautifulSoup(req.content, 'html.parser')
  List = []
  for link in soup.find_all("b", class_="uk-heading-bullet"):
    Plink = link.parent()
    
    title = str(Plink.find("b"))
    # Alink = str(Plink.find("a")['href'])
    # AAlink = str(Plink.find("a")['href'])[Alink.index('url='):]

    game = {
      "title": title,
      # "link": AAlink,
    }

    List.append(game)
  return List

print(getLinkList(getSearchList('UNO')[5]['link']))