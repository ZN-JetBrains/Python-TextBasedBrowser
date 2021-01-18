# Author: Zaid Neurothrone

from colorama import init, deinit, Fore
from bs4 import BeautifulSoup
from collections import deque
import requests
import os
import sys


class Menu:
    BACK = "back"
    EXIT = "exit"


class Browser:
    tags_list = ["title", "p", "h1", "h2", "h3", "h4", "h5", "h6", "a", "ul", "ol", "li"]

    def __init__(self):
        self.saved_websites = list()
        self.history_stack = deque()
        self.path = os.getcwd()
        self.setup_save_dir()
        init()  # Initialize colorama

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

    def save_website(self, short_url, html_text):
        self.history_stack.append(short_url)
        with open(f"{self.path}/{short_url}", "w", encoding="utf-8") as out_file:
            parsed_text = Browser.parse_html(html_text)
            # TODO: Test if writes correctly
            for line in parsed_text:
                out_file.write(line + "\n")

    def load_website(self, short_url):
        """Reads in and saves the website to the dictionary.
        """
        with open(f"{self.path}/{short_url}", "r") as in_file:
            Browser.print_parsed_website(in_file.read())

    @staticmethod
    def parse_html(html_text):
        soup = BeautifulSoup(html_text, "html.parser")
        parser = soup.find_all(Browser.tags_list, text=True)
        parsed_text = []
        for line in parser:
            if line.get("href"):
                parsed_text.append(Fore.BLUE + line.get_text().strip())
            else:
                parsed_text.append(Fore.BLACK + line.get_text().strip())
        return parsed_text

    @staticmethod
    def print_parsed_website(text):
        for line in text:
            if line:
                print(line)

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
        except requests.exceptions.ConnectionError:
            print("Incorrect URL")
        else:
            if request:
                self.saved_websites.append(self.remove_protocol(url))
                parsed_text = Browser.parse_html(request.text)
                Browser.print_parsed_website(parsed_text)
                self.save_website(Browser.remove_protocol(url), request.text)

    def process_search_input(self, user_input):
        url = user_input
        if not Browser.is_url_valid(url):
            print("Incorrect URL")
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
    deinit()  # Deactivate colorama
