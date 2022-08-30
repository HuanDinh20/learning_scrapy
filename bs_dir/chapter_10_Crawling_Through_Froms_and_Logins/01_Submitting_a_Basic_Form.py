"""
Most web forms consist of a few HTML fields, a submit button, and an action page,
where the actual form processing is done. The HTML fields usually consist of text but
might also contain a file upload or other nontext content.
Most popular websites block access to their login forms in their robots.txt file

<form method="post" action="processing.php">
First name: <input type="text" name="firstname"><br>
Last name: <input type="text" name="lastname"><br>
<input type="submit" value="Submit">
</form>

A couple of things to notice here:
1. The names of the two input fields are first
name and lastname. This is important, you need to make sure that your variable names match up.
2. The action of the form is at processing.php

Submitting a form with the Requests library can be done in four lines, including the
import and the instruction to print the content
"""
import requests

params = {'firstname': 'Huan', 'lastname': 'Dinh'}
r = requests.post("https://pythonscraping.com/pages/processing.php", data=params)
print(r.text)
