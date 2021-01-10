from collections import deque

n = int(input())
my_stack = deque()

for _ in range(n):
    input_str = input()
    if input_str == "POP":
        my_stack.pop()
    else:
        value = int(input_str.split(" ")[1])
        my_stack.append(value)

for _ in range(len(my_stack)):
    print(my_stack.pop())
