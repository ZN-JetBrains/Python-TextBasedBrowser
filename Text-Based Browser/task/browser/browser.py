# Author: Zaid Neurothrone

from collections import deque
import requests
import os
import sys


class Menu:
    BACK = "back"
    EXIT = "exit"


class Browser:

    def __init__(self):
        self.saved_websites = list()
        self.history_stack = deque()
        self.path = os.getcwd()
        self.setup_save_dir()

    def setup_save_dir(self):
        args = sys.argv
        try:
            dir_name = args[1]
            if dir_name is not None:
                self.path += f"/{dir_name}"
        except IndexError:
            self.path += "/tb_tabs"

        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def save_website(self, short_url, text):
        self.history_stack.append(short_url)
        with open(f"{self.path}/{short_url}", "w", encoding="utf-8") as out_file:
            out_file.write(text)

    def load_website(self, short_url):
        """Reads in and saves the website to the dictionary.
        """
        with open(f"{self.path}/{short_url}", "r") as in_file:
            print(in_file.read())

    @staticmethod
    def display_website(text):
        print(text)

    @staticmethod
    def is_url_valid(url):
        if url.rfind(".") == -1:
            return False
        return True

    @staticmethod
    def has_url_protocol(url):
        if url.startswith("https://"):
            return True
        return False

    @staticmethod
    def append_protocol(url):
        return "https://" + url

    @staticmethod
    def remove_protocol(url):
        return url.split("https://")[1]

    def access_website(self, url):
        try:
            request = requests.get(url)
        except IndexError:
            print("[Error]: Invalid url.")
        else:
            if request:
                self.saved_websites.append(self.remove_protocol(url))
                Browser.display_website(request.text)
                self.save_website(Browser.remove_protocol(url), request.text)

    def process_search_input(self, user_input):
        url = user_input
        if not Browser.is_url_valid(url):
            print("[Error]: Incorrect URL.")
            return

        if not Browser.has_url_protocol(url):
            if url in self.saved_websites:    # If website saved to file, render it
                self.load_website(url)
                return

        url = Browser.append_protocol(url)    # Else access website on the internet and render it
        self.access_website(url)


def run():
    browser = Browser()

    while True:
        user_input = input().lower().strip()

        if user_input == Menu.EXIT:
            break

        if user_input == Menu.BACK:
            if len(browser.history_stack) > 1:
                browser.history_stack.pop()
                short_url = browser.history_stack.pop()
                browser.load_website(short_url)
        else:
            browser.process_search_input(user_input)


if __name__ == "__main__":
    run()
