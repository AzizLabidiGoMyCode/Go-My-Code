#Q1
import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text
print(get_html('https://fr.wikipedia.org/wiki/%C3%89lections_%C3%A9lections_turques_de_2023'))
#Q2
def get_title(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1').text
    return title
print(get_title(get_html('https://fr.wikipedia.org/wiki/%C3%89lections_%C3%A9lections_turques_de_2023')))
#Q3
def get_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.find_all('p')
    text = [p.text for p in text]
    return text
print(get_text(get_html('https://fr.wikipedia.org/wiki/%C3%89lections_%C3%A9lections_turques_de_2023')))
#Q4
def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    links = [l['href'] for l in links]
    return links
#Q5
def get_all_links(url):
    html = get_html(url)
    links = get_links(html)
    return links
print(get_all_links('https://fr.wikipedia.org/wiki/%C3%89lections_%C3%A9lections_turques_de_2023'))
