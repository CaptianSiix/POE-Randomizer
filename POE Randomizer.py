import requests
import random
from bs4 import BeautifulSoup

url = "https://www.poewiki.net/wiki/List_of_skill_gems"
result = requests.get(url)
content = result.content
soup = BeautifulSoup(content, "xml")
#Removes Text that we do not want
gem_list = [x.attrs['title'] for x in
            soup.select('table.wikitable .c-item-hoverbox .c-item-hoverbox__activator > a[title]') if
            x.has_attr('title')]


#These dont change so they can be static
ascendancy_list = ["Slayer","Gladiator","Champion","Assassin","Saboteur","Trickster","Juggernaut","Berserker",
                   "Chieftain","Necromancer","Occultist","Elementalist",'Deadeye','Raider','Pathfinder','Inquisitor',
                   'Hierophant','Guardian','Ascendant']


#Asks what character you want then what skills you can use.
ascendancy_choice = int(input("How many choices of ascendancies would you like? " ))
for x in range(ascendancy_choice):
    print(random.choice(ascendancy_list))
gem_amount = int(input("\nHow many active skill gems including auras would you like? " ))

for x in range(gem_amount):
    print(random.choice(gem_list))

