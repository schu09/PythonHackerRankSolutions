def is_leap(year):
    leap = False
    if year % 4 == 0:  # True
        leap = True
    if (year % 100 == 0) or (year % 400 == 0):
        leap = False
    if (year % 100 == 0) and (year % 400 == 0):
        leap = True
    return leap

year = int(input())
print(is_leap(year))