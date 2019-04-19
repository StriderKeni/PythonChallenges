import requests
from bs4 import BeautifulSoup

re = requests.get('https://genius.com/Mina-knock-gettin-mine-lyrics')
text = BeautifulSoup(re.text)

print(text.find('div', {'class': 'lyrics'}).get_text())
