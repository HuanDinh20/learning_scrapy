import os
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

downloadDirectory = 'downloaded'
baseUrl = 'http://pythonscraping.com'


def getAbsoluteUrl(baseUrl, source):
    if source.startswith('https://www.'):
        url = f'https://www.{source[12:]}'
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = source[4:]
        url = f'https://{source}'
    else:
        url = f'{baseUrl}/{source}'
    if baseUrl not in url:
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    print('<>' * 10)
    print('absoluteUrl:', absoluteUrl)
    path = absoluteUrl.replace('www.', '')
    print('>< >< ><' * 10)
    print('path 1:', path)
    print('*' * 20)
    path = path.replace(baseUrl, '')
    print('path 2:', path)
    print(' - - - '*10)
    path = downloadDirectory + path
    print('path 3:', path)
    directory = os.path.dirname(path)
    print('directory:', directory)
    if not os.path.exists(directory):
        os.makedirs(directory)

    return path

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
downloadList = bs.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteUrl(baseUrl, download['src'])
    if fileUrl is not None:
        print('+-+-+-+-+--+'*10)
        print(fileUrl)

urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
