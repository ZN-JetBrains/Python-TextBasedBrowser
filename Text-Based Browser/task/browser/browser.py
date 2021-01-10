# Author: Zaid Neurothrone

from collections import deque
import os
import sys

nytimes_com = '''This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

websites = {"nytimes": nytimes_com, "bloomberg": bloomberg_com}
saved_urls = []
path = os.getcwd()

my_stack = deque()


def is_valid_url(a_url):
    if a_url.rfind(".com") == -1:
        return False
    return True


def save_website(a_url):
    global path
    my_stack.append(a_url)
    with open(f"{path}/{a_url}", "w", encoding="utf-8") as out_file:
        out_file.write(websites[a_url])


def load_website(a_url):
    global path
    with open(f"{path}/{a_url}", "r", encoding="utf-8") as in_file:
        print(in_file.read())


def run():
    args = sys.argv
    global path
    try:
        dir_name = args[1]
        if dir_name is not None:
            path += f"/{dir_name}"
    except IndexError:
        path += "/tb_tabs"

    if not os.path.exists(path):
        os.mkdir(path)

    while True:
        user_input = input().lower()

        if user_input == "exit":
            break

        if user_input == "back":
            if len(my_stack) > 1:
                my_stack.pop()
                load_website(my_stack.pop())
            continue

        if user_input in saved_urls:
            load_website(user_input)
        elif is_valid_url(user_input):
            url = user_input.split(".")[0]
            saved_urls.append(url)
            if url not in websites.keys():
                print("[Error]: Url not found.")
            else:
                print(websites[url])
                save_website(url)
        else:
            print("[Error]: Incorrect URL.")


if __name__ == "__main__":
    run()
