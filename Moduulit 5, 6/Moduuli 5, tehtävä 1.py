import random

nopat = int(input("Monta noppaa heitetään ? : "))
summat = 0
for i in range(nopat):
    luku = random.randint(1, 6)
    summat += luku
print(f"Noppien silmälukujen summa on {summat}.")