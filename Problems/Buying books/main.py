from collections import deque

books_cnt = int(input())

my_stack = deque()

for _ in range(books_cnt):
    user_input = input()
    if user_input == "READ":
        print(my_stack.pop())
    else:
        book_name = user_input.split("BUY ")[1]
        my_stack.append(book_name)
