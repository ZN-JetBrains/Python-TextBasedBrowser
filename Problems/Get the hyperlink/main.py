import requests

from bs4 import BeautifulSoup

act = int(input())
url = input()

# Tests
# act = 3
# url = "http://www.gutenberg.org/files/3825/3825-h/3825-h.htm"

req = requests.get(url)
if req:
    soup = BeautifulSoup(req.content, "html.parser")
    link = soup.find("a", text=f"ACT {act}").get("href")
    print(link)

    # links = soup.find_all("a")
    # index = 0
    # for _ in range(len(links)):
    #     if index == act - 1:
    #         print(links[index].get("href"))
    #     index += 1
