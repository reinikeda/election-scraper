from bs4 import BeautifulSoup
import requests

url = 'https://www.delfi.lt'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.find_all(class_='headline-title'))