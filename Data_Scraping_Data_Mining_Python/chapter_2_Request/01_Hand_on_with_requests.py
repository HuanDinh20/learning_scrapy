import requests

r = requests.get('https://quotes.toscrape.com/')
print(r.status_code)
print(r.text)