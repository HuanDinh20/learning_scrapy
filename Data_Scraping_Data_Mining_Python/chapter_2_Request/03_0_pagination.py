import requests

r = requests.get('https://quotes.toscrape.com/page/2/')

save_path = r'A:\huan_shit\learning_scrapy\Data_Scraping_Data_Mining_Python\chapter_2_Request\03_all_author.text'
for i in range(1,11):
    r = requests.get(f'https://quotes.toscrape.com/page/{i}/')
    html = r.text
    with open(save_path, 'a', encoding='utf-8') as f:
        for line in html.split('\n'):
            if '<span class="text" itemprop="text">' in line:
                line = line.replace('<span class="text" itemprop="text">“', '"').replace('”</span>', '"')
                line = line.strip()
                f.write(line)
                f.write('\n')