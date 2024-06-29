# Tenho que retornar o título, e conteúdo do artigo

import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser

headers = {'user-agent': 'Mozila/5.0'}

# Acessando página mais simples para extrapolação das outras
URL = "https://realpython.github.io/fake-jobs/" 
#pagina = requests.get(URL) 

# Teste com página real

URL1 = "https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.htmL"
URL2 = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/"
URL3 = "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"
URL4 = "https://www.reuters.com/article/us-health-coronavirus-global-deaths/global-coronavirus-deaths-pass-agonizing-milestone-of-1-million-idUSKBN26K08Y"
lista_url = [URL1, URL2, URL3, URL4]

requisicoes = []

for urls in lista_url:
    urls = requests.get(urls, headers=headers)
    requisicoes.append(urls)

print(requisicoes)

    


'''
print(pagina1.status_code) # Primeira conexão - OK (200)
#print(pagina2.status_code)# Conexão site real - OK (200)

soup = BeautifulSoup(pagina1.content, "html.parser")

resultado = soup.find("h1")

print(len(lista_url))

for texto in resultado:
    print(resultado.text, end="\n"*2)
#print(resultado.prettify())
'''