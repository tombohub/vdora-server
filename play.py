import requests
import json
from bs4 import BeautifulSoup

with open('data.json') as file:
    email_json = json.loads(file.read())

email_body_html = email_json['HtmlBody']
soup = BeautifulSoup(email_body_html, 'html.parser')

print(soup.prettify())
