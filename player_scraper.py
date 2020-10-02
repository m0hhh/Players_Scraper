import requests
from bs4 import BeautifulSoup

code = input('Enter webpage URL: ')

source = requests.get(code).text

soup = BeautifulSoup(source, 'lxml')

players = soup.find_all('a', class_='playerName')
club = soup.find('div', class_='current')

print(club)


# for player in players:
#     playerName = player.text
#     print(playerName)









 
