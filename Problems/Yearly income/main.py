# write your code here
with open("salary_year.txt", "w", encoding="utf-8") as out_file:
    with open("salary.txt", "r") as in_file:
        for line in in_file:
            monthly_salary = int(line.strip("\n"))
            out_file.write(str(monthly_salary * 12) + "\n")
