import shelve
import re
from bs4 import BeautifulSoup

db = shelve.open("champions")

# TODO: grep from online
with open("champions.htm") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
champions = soup.find_all("a", class_="block tooltip tooltipstered")

for champ in champions:
    name = re.search(r"(?<=data-id\=\")(\w+)", str(champ))
    link = re.search(r"(?<=href\=\")(.+)(?=\")", str(champ))

    db[name.group()] = link.group()
    # print(name.group(), link.group())

db.close()
