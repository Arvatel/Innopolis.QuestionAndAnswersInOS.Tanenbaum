import random

with open("input", "w") as f:
    for i in range(0, 1000):
        print(random.randint(1, 501), end=" ", file=f)
