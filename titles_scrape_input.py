from bs4 import BeautifulSoup
import requests

def scrape_titles(url, website_name, desired_person, title_class):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    all_titles = soup.find_all(class_=title_class)

    for title in all_titles:
        title_text = title.text.strip()
        if desired_person[1].lower() in title_text.lower():
            print(f'Match found! {website_name}: {title_text}')

website_data = {
    'https://www.lrt.lt': {'title_class': 'news__title', 'name': 'LRT'},
    'https://www.15min.lt': {'title_class': 'vl-title', 'name': '15MIN'},
    'https://www.delfi.lt': {'title_class': 'headline-title', 'name': 'DELFI'},
    'https://www.lrytas.lt': {'title_class': 'LPostContent__title', 'name': 'LRYTAS'},
}

desired_persons = {
    1: ['Gitanas Nausėda', 'nausėd'],
    2: ['Arvydas Anušauskas', 'anušausk'],
    3: ['Vilija Blinkevičiūtė', 'blinkevičiūt'],
    4: ['Saulius Skvernelis', 'skvernel'],
    5: ['Ingrida Šimonytė', 'šimonyt'],
    6: ['Viktorija Čmilytė-Nielsen', 'čmilyt'],
}

while True:
    print('*** Choose a desired person to scrape ***')
    for key, person in desired_persons.items():
        print(f'{key}: {person[0]}')
    print('0: Exit')
    choice = int(input('Enter the corresponding number: '))

    if choice == 0:
        break
    elif choice in desired_persons:
        chosen_desired_person = desired_persons[choice]

        print(f'Scraping for {chosen_desired_person[0]}...')
        for url, data in website_data.items():
            scrape_titles(url, data['name'], chosen_desired_person, data['title_class'])
    else:
        print('Invalid choice. Please choose a valid number.')