x, y, z, n = (int(input())for _ in range(4))  # Stores the input of 4 values
perms = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

print(perms)
