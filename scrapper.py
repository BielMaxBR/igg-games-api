import requests
from bs4 import BeautifulSoup
import re

link = "https://www.igg-games.com/"
req = requests.get(link)

def gamesearch(search):
    list = []

    print('Requisição bem sucedida!')
    # fazendo a pesquisa
    
    
    req_pes = requests.get(link+"?s={}".format(search))

    content = req_pes.content

    soup = BeautifulSoup(content, 'html.parser')
    conteudo = []
    # print(soup.find_all(class_="uk-container"))
    grid = soup.body.find("div", class_=re.compile("uk-width-expand"))
    for post in grid.contents: #"a", id=re.compile('post')):        
        print(post)
        arquivo = open('post.txt', 'w')
        conteudo.append(str(post)) 
        arquivo.writelines(conteudo)
        arquivo.close()
        # thumb = str(post.find("img")
        # linkPost = str(post.find("a", class_="uk-link-reset")['href']).replace("https://", "https://www.")
        # name = str(post.find("a", class_="uk-link-reset").string)
        # details = []
        # HE = post.find("p", class_="uk-article-meta")
        # print(post)
        # for i in HE.find_all_next():
        #     details += [i.string]
        # list += [thumb, linkPost, name, details] 

        # for i in list:
        #     print(list[list.index(i)])
    
    return list
# conectando no site

def linksearch(game):
    req_jogo = requests.get(game)
    content = req_jogo.content
    soup = BeautifulSoup(content, 'html.parser') 
    nomes = []
    links = []
    
    
    count = 0
    # pegando o link   
    for tag in soup.body.find_all("p", style="line-height: 8%;"):           
        teg = tag.find_previous("p")
        try:
            link = teg.find("a", href=re.compile("bluemediafiles"))['href']
            
            if link != None:
                nome = teg.find("b").string
                plink = str(link)[8:]
                pplink = plink[plink.index('://')+3:]
                #print("[{}]".format(count)+nome)
                nomes += [nome]
                links += [pplink]
            count += 1
            print("foi")
        except:
            None
        

    ultimo = tag.find_next('p')
    
    try:
        link = ultimo.find("a", href=re.compile("bluemediafiles"))['href']      
        if link != None:            
            nome = ultimo.find("b").string
            plink = str(link)[8:]
            pplink = plink[plink.index('://')+3:]
            #print("[{}]".format(count)+nome)        
            nomes += [nome]
            links += [pplink]
            print("foi")
    except:
        None
    return links, nomes
    

if req.status_code == 200:
    pesquisa = str("VVVVVV").replace(" ", "+") # input("jooj: ")
   
    # colocar um selecionador de jogos numa lista
    link_game = gamesearch(pesquisa)
    # link_download = linksearch(link_game)[0]
    # nome_download = linksearch(link_game)[1]
    # print(type(link_game))
    # for i in link_game:
    #     print(link_game[link_game.index(i)])


    # for i in nome_download:
    #     print('[{}]'.format(nome_download.index(i)), nome_download[nome_download.index(i)])

    # escolha = int(input("qual dos links você quer?: "))

    # print("Link pra download: \n"+link_download[escolha])
