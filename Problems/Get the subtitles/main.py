import requests

from bs4 import BeautifulSoup

n = int(input())
url = input()

# Tests
# n = 1
# url = "https://www.grammarly.com/blog/articles/"

req = requests.get(url)
if req:
    soup = BeautifulSoup(req.content, "html.parser")
    subtitles = soup.find_all("h2")
    index = 0
    for _ in range(len(subtitles)):
        if index == n:
            print(subtitles[index].text)
        index += 1
