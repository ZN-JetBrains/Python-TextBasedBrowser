import requests

from bs4 import BeautifulSoup

search_word = input()
url = input()

req = requests.get(url)
if req:
    soup = BeautifulSoup(req.content, "html.parser")
    paragraphs = soup.find_all("p")

    for p in paragraphs:
        if search_word in p.text:
            print(p.text)
            break
