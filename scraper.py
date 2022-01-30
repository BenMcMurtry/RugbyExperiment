import pandas as pd
from bs4 import BeautifulSoup
import requests

url="http://stats.espnscrum.com/statsguru/rugby/stats/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup)

from lxml import etree
table = etree.HTML(soup).find("body/table")
rows = iter(table)
headers = [col.text for col in next(rows)]
for row in rows:
    values = [col.text for col in row]
    print(dict(zip(headers, values)))
