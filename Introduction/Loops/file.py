n = int(input())
if n > 20:
    exit()  # Allows us to end the program if the condicion is met
else:
    for i in range(n):
        print(pow(i, 2))  # The pow() function returns the value of x to the power of y 
