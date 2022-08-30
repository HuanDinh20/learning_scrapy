"""
1. jQuery
jQuery is an extremely common library, used by 70% of the most popular internet
sites and about 30% of the rest of the internet.1
 A site using jQuery is readily identifia‐
ble because it will contain an import to jQuery somewhere in its code:
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></
 script>
 If jQuery is found on a site, you must be careful when scraping it. jQuery is adept at
dynamically creating HTML content that appears only after the JavaScript is exe‐
cuted. If you scrape the page’s content by using traditional methods, you will retrieve
only the preloaded page that appears before the JavaScript has created the content
2. Google Analytics
Google Analytics is used by about 50% of all websites, making it perhaps the most
common JavaScript library and the most popular user tracking tool on the internet.
Determining whether a page is using Google Analytics is easy. It will have JavaScript
at the bottom, similar to the following:
<script type="text/javascript">
This script handles Google Analytics–specific cookies used to track your visit from
page to page. This can sometimes be a problem for web scrapers that are designed to
execute JavaScript and handle cookies
If a site uses Google Analytics or a similar web analytics system, and you do not want
the site to know that it’s being crawled or scraped, make sure to discard any cookies
used for analytics or discard cookies altogether
3. Ajax and Dynamic HTML
Until now, the only way we’ve had of communicating with a web server is to send it
some sort of HTTP request via the retrieval of a new page. If you’ve ever submitted a
form or retrieved information from a server without reloading the page, you’ve likely
used a website that uses Ajax
Contrary to what some believe, Ajax is not a language but a group of technologies
used to accomplish a certain task

"""
from selenium import webdriver
import requests

executable_path=r"A:\huan_shit\learning_scrapy\bs_dir\chrome_sele\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=executable_path)
driver.get('https://productionvn.akselos.com:9020/training_time_predict_projects')

"""
https://productionvn.akselos.com:9020/
r = requests.get('https://productionvn.akselos.com:9020', auth=('huandinh2022', '27081996'))
"""