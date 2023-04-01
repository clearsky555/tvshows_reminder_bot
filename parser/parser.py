from datetime import datetime

import requests
from bs4 import BeautifulSoup

from database import TVShowsManager, engine


manager = TVShowsManager(engine=engine)


def get_html(URL):
    response = requests.get(URL)
    return response.text


URL = 'https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv'
html = get_html(URL)

soup = BeautifulSoup(html, 'html.parser')
content = soup.find('div', {'class':'lister'}).find('tbody', {'class':'lister-list'})
shows = content.find_all('tr')


def write_data(data):
    result = manager.insert_show(data)
    return result


def main():
    for i, s in enumerate(shows, start=1):
        title = s.find('td', {'class': 'titleColumn'}).find('a').text
        year = s.find('td', {'class': 'titleColumn'}).find('span').text
        rating = s.find('td', {'class': 'ratingColumn'}).text.strip()
        href = s.find('a').get('href')
        full_url = 'https://www.imdb.com' + href
        data = {
            'place':i,
            'title':title,
            'year':year,
            'rating':rating,
            'link':full_url
        }
        write_data(data)


def launching_parser():
    print('запустился парсер')
    manager.delete_table()
    manager.create_table()
    main()


def get_show_data(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('section', {'class': 'border_all_dashed'})
    title = soup.find('header', {'class': 'pagehead'}).find('h1').text.strip()
    try:
        date_tag = content.find('time', {'class':'c_g2'})
        date_string = date_tag.get('datetime')
        try:
            date = datetime.strptime(date_string, '%Y-%m-%d')
            return [url, date, title]
        except ValueError:
            return [url, 'данных о выходе новых серий нет', title]
    except AttributeError:
        return [url, 'данных о выходе новых серий нет', title]


# def get_show_title(url):
#     html = get_html(url)
#     soup = BeautifulSoup(html, 'html.parser')
#     content = soup.find('header', {'class': 'pagehead'})
#     title = content.find('h1').text.strip()
#     return title