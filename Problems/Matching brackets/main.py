sample_input = input()

index = 0
left_brackets = []
right_brackets = []

for _ in range(len(sample_input)):
    if sample_input[index] == "(":
        left_brackets.append(index)
    elif sample_input[index] == ")":
        right_brackets.append(index)
    index += 1


is_valid = True
if len(left_brackets) != len(right_brackets):
    is_valid = False
else:
    index = 0
    for _ in range(len(left_brackets)):
        if left_brackets[index] > right_brackets[index]:
            is_valid = False
            break

print("OK" if is_valid else "ERROR")
