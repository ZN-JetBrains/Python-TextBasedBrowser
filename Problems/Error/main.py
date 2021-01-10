with open('years.txt', 'w', encoding='utf-8') as f:
    for i in range(2010, 2020 + 1):
        f.write(str(i) + " ")
