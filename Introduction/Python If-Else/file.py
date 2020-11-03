number = int(input())
if number >= 1 & number <= 100:
    if number % 2 != 0:
        print("Weird")
    else:
        if 2 <= number <= 5:
            print("Not Weird")
        if 6 <= number <= 20:
            print("Weird")
        if number > 20:
            print("Not Weird")
