"""
Most modern websites use cookies to keep track of who is logged in and who is not.
After a site authenticates your login credentials, it stores them in your browser’s
cookie, which usually contains a server-generated token, time-out, and tracking
information.
Although cookies are a great solution for web developers, they can be problematic for
web scrapers.
"""

import requests

params = {'username': 'Huan', 'password': 'password'}
r = requests.post('https://pythonscraping.com/pages/cookies/welcome.php', params)
print('Cookie is seted to: ')
print(r.cookies.get_dict())
print('Going to profile page...')
r = requests.get('https://pythonscraping.com/pages/cookies/profile.php',cookies=r.cookies)
print(r.text)
"""
This works well for simple situations, but what if you’re dealing with a more compli‐
cated site that frequently modifies cookies without warning, or if you’d rather not
even think about the cookies to begin with? The Requests session function works
perfectly in this case:
"""
session = requests.Session()
s = session.post('https://pythonscraping.com/pages/cookies/welcome.php', params)
print('Cookie is set to:')
print(s.cookies.get_dict())
print('Going to profile page...')
s = session.get('http://pythonscraping.com/pages/cookies/profile.php')
print(s.text)