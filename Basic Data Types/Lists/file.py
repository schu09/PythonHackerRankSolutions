n = int(input())
crazy_list = []

for _ in range(n):
    name_of_command, *ints_of_command = input().split()  # takes the name of the command and the numbers if any
    name_of_command.lower()  # transforms the name of the command into lowercase
    list_of_ints = list(map(int, ints_of_command))  # transforms the list of numbers from str to int

    # commands:
    if name_of_command == "append":
        crazy_list.append(list_of_ints[0])

    if name_of_command == "insert":
        crazy_list.insert(list_of_ints[0], list_of_ints[1])

    elif name_of_command == "print":
        print(crazy_list)

    elif name_of_command == "remove":
        crazy_list.remove(list_of_ints[0])

    elif name_of_command == "sort":
        crazy_list.sort()

    elif name_of_command == "pop":
        crazy_list.pop()

    elif name_of_command == "reverse":
        crazy_list.reverse()
