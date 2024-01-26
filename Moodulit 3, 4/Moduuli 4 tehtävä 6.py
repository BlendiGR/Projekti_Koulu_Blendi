import random

N = n = 0

while N < 1000:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    N += 1
    print("Arvottu piste: \n")
    if x * x + y * y < 1:
        n += 1
print(f"Pisteitä yhteensä {N}, joista ympyrän sisällä {n}!")

