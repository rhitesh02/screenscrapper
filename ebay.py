#!/usr/bin/env python

__author__ = "Hitesh Rathod"
__copyright__ = "Copyright 2020, The screen scrapper Project"
__version__ = "1.0.1"
__email__ = "rhitesh@yahoo.com"
__status__ = "Production"


import requests, sys
from bs4 import BeautifulSoup
import csv

# returns soup object if URL resonds
def get_page(url):
    response = requests.get(url)
    if not response.ok:
        print('server responded:', response.status_code)
    else:
        soup = BeautifulSoup(response.text, features="html.parser")
    return soup

# parse HTML tags
def get_data_detail(soup):
  
    try:
        title = soup.find('h1', id='itemTitle').text.strip().split('  \xa0')[1]
    except:
       title = ''
    
    try:
        p = soup.find('span', id='prcIsum').text.strip()
        currency, price = p.split(' ')
    except:
        currency = ''
        price = ''

    try:
        sold = soup.find('span', class_='vi-qtyS-hot-red').find('a').text.strip().split(' ')[0]
    except:
        sold = ''

    data = {
        'title': title, 
        'price': price,
        'currency':currency,
        'total sold':sold

    }
    return data

# find all URL Links to loop thru   
#  returns list of URLS
def get_index_data(soup):
    try:
        links = soup.find_all('a', class_='s-item__link')
    except:
        links = []

    urls = [item.get('href') for item in links ]
    return urls  

# Write screen scrapper output to csv file
def write_csv(file_name, data, url):
    #schema = ['Title','Price','Currency','toatl_sold', 'URL']
    file_name = file_name + '.csv'
    with open(file_name, 'a', encoding="utf-8",  newline='') as csvfile:
        writer = csv.writer(csvfile)        
        row = [data['title'], data['price'], data['currency'], data['total sold'], url]
        writer.writerow(row)

# Calling main function
#  Here lies the call routings
def main():

    search_string = sys.argv[1]
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='+ search_string +'&_sacat=0&_pgn=1'
 
    products = get_index_data(get_page(url))

    for link in products:
        data = get_data_detail(get_page(link))
        write_csv(search_string, data, link)


if __name__ == "__main__":
    main()