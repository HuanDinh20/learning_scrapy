from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')

datafile = StringIO(data)
csvReader = csv.reader(datafile)

for row in csvReader:
    print(row)