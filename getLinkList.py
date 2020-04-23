import requests
from bs4 import BeautifulSoup
import re
from getSearchList import getSearchList

# game = URL do game no igg-games.com
def getLinkList(game):
  req = requests.get(f'{game}')
  print(req.status_code)
  soup = BeautifulSoup(req.content, 'html.parser')
  List = []
  for link_list in soup.find_all("b", class_="uk-heading-bullet"):
    Plink = link_list.parent()
    # Plink = Plink[0]
    title = str(Plink[0].string)
    link = Plink[2]
    if str(link).count('blue') != 0:
        print(str(link).count('blue'))
        finalLink = str(link['href'])[60:]
    else:
        print('adfly', str(link).count('blue'))
        print('#'*60)
        finalLink = str(link['href'])
    print('Link=', finalLink)
    print('$'*60)
    # finalLink = link['href']
    game = {
      "title": title,
      "link": finalLink,
    }

    List.append(game)
  return List
"""
USkSn82FylsejFCipVsahU2r2FXfgX2LgYHme3?xurl=


jFCipVhU2r2FXX2LgYHme3?xurl=
jFCipVhU2r2FXX2LgYHme3?xurl=
jFCipVhU2r2FXX2LgYHme3?xurl=
jFCipVhU2r2FXX2LgYHme3?xurl=
jFCipVhU2r2FXX2LgYHme3?xurl=
"""