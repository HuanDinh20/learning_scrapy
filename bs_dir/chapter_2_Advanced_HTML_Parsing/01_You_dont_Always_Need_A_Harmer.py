from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html5lib')
try:
    bs.find_all('table')[4].find_all('tr')[2].find('td').find_all('div')[1].find('a')
except:
    print(" keep in mind that layering the techniques used in this section with reckless abandon can"
          " lead to code that is difficult to debug, fragile, or both. "
          "Before getting started, "
          "let’s take a look at some of the ways you can avoid altogether the need for advanced HTML parsing! " )

"""
. What if the site’s web developer decides to add another table or another col‐
umn of data?
. What if the developer adds another component (with a few div tags) to the top of the page? 
The preceding line is precarious and depends on the structure of
the site never changing
So what are your options
1. Look for a “Print This Page” link, or perhaps a mobile version of the site that has
better-formatted HTML 
2. Look for the information hidden in a JavaScript file. Remember, you might need
to examine the imported JavaScript files in order to do this.
3. This is more common for page titles, but the information might be available in
the URL of the page itself.
4.  If the information you are looking for is unique to this website for some reason,
you’re out of luck. If not, try to think of other sources you could get this informa‐
tion from. Is there another website with the same data? Is this website displaying
data that it scraped or aggregated from another website?


"""