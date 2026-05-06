def is_year_leap(x):
    if x % 4 == 0:
        return True
    else:
        return False

year = int(input("Введите год: "))
result = is_year_leap(year)

print("год", year, ":", result)