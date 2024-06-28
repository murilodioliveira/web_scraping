import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser

# Acessando página mais simples para extrapolação das outras
URL = "https://realpython.github.io/fake-jobs/" 
pagina = requests.get(URL) 

# Teste com página real
URL2 = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/"
#pagina2 = requests.get(URL2)


#print(pagina.status_code) # Primeira conexão - OK (200)
#print(pagina2.status_code)# Conexão site real - OK (200)

soup = BeautifulSoup(pagina.content, "html.parser")

resultado = soup.find("h1",class_="title is-1")
print(resultado.prettify())