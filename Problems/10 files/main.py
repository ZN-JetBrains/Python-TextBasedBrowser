for i in range(1, 10 + 1):
    file_name = "file" + str(i) + ".txt"
    with open(file_name, "w", encoding="utf-8") as out_file:
        out_file.write(str(i))
