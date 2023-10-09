import requests
from bs4 import BeautifulSoup

url = 'https://www.flashscore.se/shl/#/KYa5vZpK/table/overall'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find().find('div', id='tournament-table')
rows = table.findAll('div', classmethod='ui-table__row  ')
rows = table.findAll('div')
print(rows)