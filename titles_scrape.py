from bs4 import BeautifulSoup
import requests

def scrape_titles(url, website_name, desired_person, title_class):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    all_titles = soup.find_all(class_=title_class)

    for title in all_titles:
        title_text = title.text.strip()
        if desired_person[1].lower() in title_text.lower():
            print(f'{website_name}: {title_text}')

website_data = {
    'https://www.lrt.lt': {'title_class': 'news__title', 'name': 'LRT'},
    'https://www.15min.lt': {'title_class': 'vl-title', 'name': '15MIN'},
    'https://www.delfi.lt': {'title_class': 'headline-title', 'name': 'DELFI'},
    'https://www.lrytas.lt': {'title_class': 'LPostContent__title', 'name': 'LRYTAS'},
}

desired_person = ['Gitanas Nausėda', 'nausėd']

for url, data in website_data.items():
    print(f'Scraping for {desired_person[0]}...')
    scrape_titles(url, data['name'], desired_person, data['title_class'])
