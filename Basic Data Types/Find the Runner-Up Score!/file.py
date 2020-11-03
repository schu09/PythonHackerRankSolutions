n = int(input())
lista = list(map(int, input().split()))

if (n < 2 or n > 10) or (n != len(lista)):
    exit()

for n in range(len(lista)):
    if (lista[n] < -100) or (lista[n] > 100):
        exit()

z = max(lista)                    # z stores the value of the biggest number
while max(lista) == z:            # compares if the max number is still in the list
    lista.remove(max(lista))      # removes the max number set at the beggining, but not the next max number

print(max(lista))
