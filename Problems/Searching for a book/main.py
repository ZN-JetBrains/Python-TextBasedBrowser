import requests


def do_search(bookstore_url, params):
    return requests.get(bookstore_url, params=params)


# do_search("http://bookstore.com/search", {"author": "Austen", "title": "Emma"})
