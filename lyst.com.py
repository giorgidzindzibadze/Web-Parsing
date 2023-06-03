import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv

url = 'https://www.lyst.com/shop/mens-sneakers/?'
payload={'page':1}
h = {'Accept-Language': 'en-US'}
file = open('LYST.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['ბრენდი', 'ფასი', 'დამატებითი ინფორმაცია','რომელი საიტიდან იყიდება'])


while payload['page']<=6:
    response = requests.get(url,params=payload, headers=h)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    shoes_soup = soup.find('div', class_='lyst-app__layout-container lyst-app__layout-container--no-top-white-space')

    all_shoes = shoes_soup.find_all('div',class_='lW9iE')
    for shoe in all_shoes:
        right_block = shoe.find('div', class_='bqic2g1 bqic2g5 _1b08vvh54 _1b08vvh5k')
        title=right_block.find('span',class_='_1b08vvh1n _1b08vvhk8 vjlibs5 vjlibs2').text
        price = right_block.find('div',class_='_1b08vvhk4 vjlibs2').text
        desc=right_block.find('div',class_='_1jn5ix24').text
        site=right_block.find('span',class_='_1b08vvh1n _1b08vvhk8 vjlibs2').span.text
        print(f'{title},  {price},  {desc},  {site}')
        csv_obj.writerow([title, price, desc, site])
    payload['page'] += 1
    sleep(randint(15,20))
file.close()