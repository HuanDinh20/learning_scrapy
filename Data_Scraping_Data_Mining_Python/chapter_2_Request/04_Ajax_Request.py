import requests
import json
url = r'https://www.espn.com/nfl/'
r = requests.get(url)
# if class = str, them import json
# print(type(r.text))
data = json.loads(r.text)
print(data)
print('>>>>', type(data))

