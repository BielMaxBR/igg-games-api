import requests
from bs4 import BeautifulSoup
import re

link = "https://www.igg-games.com/"
print("iniciando...\n")
def getSearchList(search):
  req = requests.get(f'{link}?s={search}')
  soup = BeautifulSoup(req.content, 'html.parser')
  List = [] 

  for game in soup.find_all("article", class_="post"):
    #gameContents = game.find_parent().find_parent()
  
    List.append(game)
  return List
print(getSearchList('Uno')[5])
# def gamesearch(search):
#     print('Requisição bem sucedida!')
#     # fazendo a pesquisa
    
    
#     req_pes = requests.get(link+"?s={}".format(search))

#     content = req_pes.content

#     soup = BeautifulSoup(content, 'html.parser')

#     return str(soup.body.find("a", class_="uk-link-reset")['href']).replace("https://", "https://www.")
# # conectando no site