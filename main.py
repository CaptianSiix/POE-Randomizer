import requests
from bs4 import BeautifulSoup

#Definitions
url = "https://www.poewiki.net/wiki/List_of_skill_gems"
result = requests.get(url)

content = result.content
soup = BeautifulSoup(content, "xml")

#Gets gem list From the website... They are updated often so this keeps them current
gem_list = soup.find_all("a", limit=12)

#Prints Gems
print(gem_list)
for gem in gem_list:
    print(gem.get_text())

