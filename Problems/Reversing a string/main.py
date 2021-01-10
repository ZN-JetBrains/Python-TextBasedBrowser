n = int(input())

my_stack = []
for _ in range(n):
    my_stack.append(input())

for _ in range(n):
    print(my_stack.pop())
