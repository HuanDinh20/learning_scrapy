import requests

r = requests.get('https://quotes.toscrape.com/')
html = r.text
with open(r'A:\huan_shit\learning_scrapy\Data_Scraping_Data_Mining_Python\chapter_2_Request\quotes.txt', 'w') as f:
    for line in html.split('\n'):
        if '<span class="text" itemprop="text">' in line:
            line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '')
            line = line.strip()
            f.write(line)
            f.write('\n')
