''' Nessa aula veremos como usar o BeautifulSoup para
extrair informações(raspagem de dados) de uma página HTML.
'''
from bs4 import BeautifulSoup
from pathlib import Path

html_path = Path('Pagina.html')
if not html_path.exists():
    html_path = Path('Pagina Hashtag.html')

if not html_path.exists():
    raise FileNotFoundError('Nenhum arquivo HTML encontrado. Coloque o arquivo no mesmo diretório ou ajuste o nome.')

with open(html_path, 'r', encoding='utf-8') as f:
    site = BeautifulSoup(f.read(), 'html.parser')

#print(site.prettify())
titulo = site.title 
print(titulo)
print(titulo.text)

print(site.h1)
print(site.h1.text)

print(site.h2)
print(site.h2.text)

print(site.p)
print(site.p.text)

print(site.p.attrs)
barra_navegacao = site.find('nav')
print(barra_navegacao.prettify()) 

link = barra_navegacao.find("a")
links = barra_navegacao.find_all("a")
print(link)
print(links)
print(links[1]) 
print(links[0].attrs) 
url_link = links[0]['href'] 
print(url_link) 
for link in links:
    print(link['href'])
    