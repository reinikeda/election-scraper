# deeper scrape to get text from filtered articles

from bs4 import BeautifulSoup
import requests


def scrape_titles(url, website_name, desired_person, article_title, article_date, article_lead_text):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    all_titles = soup.find_all(class_=article_title)
    all_dates = soup.find_all(class_=article_date)

    for title, date in zip(all_titles, all_dates):
        title_text = title.text.strip()
        date_text = date.text.strip()

        link_element = title.find('a')
        relative_link = link_element['href'] if link_element else ''

        if relative_link.startswith('http'):
            full_link = relative_link
        else:
            full_link = f'{url}{relative_link}'

        if desired_person[1].lower() in title_text.lower():
            # print basic detais
            print(f'{website_name}: {date_text} - {title_text} (Click here: {full_link})')

            # more info from article
            article_response = requests.get(full_link)
            article_soup = BeautifulSoup(article_response.content, 'html.parser')

            article_text_lead = article_soup.find(class_=article_lead_text)
            if article_text_lead:
                print(f'Article Text: {article_text_lead.text.strip()}')
            else:
                print('Article Text not found')


website_data = {
    'https://www.lrt.lt': {'article_date': 'info-block__text', 'article_title': 'news__title', 'article_lead_text': 'text-lead', 'name': 'LRT'},
    'https://www.15min.lt': {'article_date': '', 'article_title': 'vl-title', 'article_lead_text': 'intro', 'name': '15MIN'},
    # 'https://www.delfi.lt': {'article_date': '', 'article_title': 'headline-title', 'article_lead_text': 'C-fragment-html--text', 'name': 'DELFI'},
    'https://www.lrytas.lt': {'article_date': '', 'article_title': 'LPostContent__title', 'article_lead_text': 'LArticleHeadline__summary', 'name': 'LRYTAS'},
}

desired_person = ['Gitanas Nausėda', 'nausėd']

for url, data in website_data.items():
    print(f'Scraping for {desired_person[0]}...')
    scrape_titles(url, data['name'], desired_person, data['article_title'], data['article_date'], data['article_lead_text'])
