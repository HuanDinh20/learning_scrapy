import requests

r = requests.get('https://quotes.toscrape.com/')
html = r.text
with open(r'A:\huan_shit\learning_scrapy\Data_Scraping_Data_Mining_Python\chapter_2_Request\authors.txt', 'w') as f:
    for line in html.split('\n'):
        if '<span>by <small class="author" itemprop="author">' in line:
            line = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '')
            line = line.strip()
            f.write(line)
            f.write('\n')
