import requests
import json
from bs4 import BeautifulSoup

def scrape_wsb():
    response = requests.get("https://www.reddit.com/r/wallstreetbets/.json")
    with open("response.txt", "w") as f:
      f.write(response.text)
    rjson = response.json()
    titles = []
    for entry in (rjson["data"]["children"]):
       titles.append(entry["data"])
    print(titles)

def scrape_forbes():
   response = requests.get("https://www.forbes.com/markets/")
   html_content = response.text
   soup = BeautifulSoup(html_content, 'html.parser')
   titles = []
   for title_tag in soup.find_all('h3', class_='HNChVRGc'):
    title_text = title_tag.get_text(strip=True)
    titles.append(title_text)
   for title in titles:
    print(title)

def scrape_yahoo():
  response = requests.get("https://finance.yahoo.com/topic/stock-market-news/")
  soup = BeautifulSoup(response.text, 'html.parser')

  article_titles = soup.find_all('a', class_='mega-item-header-link')

  for title in article_titles:
    print(title.text.strip())

scrape_yahoo()
