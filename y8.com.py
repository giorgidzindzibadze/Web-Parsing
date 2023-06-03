import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv

url = 'https://www.y8.com/'
payload={'page':1}
h = {'Accept-Language': 'en-US'}
file = open('Y8.com.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['თამაშის სახელი', 'item technology', 'რეიტინგი','თამაშის რაოდენობა'])


while payload['page']<=6:
    response = requests.get(url,params=payload, headers=h)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    games_soup = soup.find('div', class_='box items-grid no-background')
    all_game = games_soup.find_all('div',class_='item thumb videobox grid-column')
    for game in all_game:
        right_block = game.find('div', class_='item__infos')
        title=right_block.h4.text
        item__technology=right_block.p.text.strip()
        rating=right_block.find('p',class_='item__rating').text.strip()
        plays_count=right_block.find('p',class_='item__plays-count').text.strip()
        print(f'{title},  {item__technology},  {rating},  {plays_count}')
        csv_obj.writerow([title, item__technology, rating, plays_count])
    payload['page'] += 1
    sleep(randint(15,20))
file.close()