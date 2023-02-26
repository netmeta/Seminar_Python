for i in range(1, 21, 2):
    print(i, end=" ")  # в строку

n = ["a", "d", "f", "y", "u"]

for i in range(len(n)):
    n[i] *= 5
print(n)

for i, v in enumerate(n, 1):  # список
    print(f"{i}) {v}")
