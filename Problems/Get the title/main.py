import requests

from bs4 import BeautifulSoup

url = input()

req = requests.get(url)
if req:
    soup = BeautifulSoup(req.content, "html.parser")
    heading = soup.find("h1")
    print(heading.text)
