luvut = []

while True:
    try:
            lukujensaaja = int(input("Anna lukuja : "))
            luvut.append(lukujensaaja)
    except ValueError:
            break

luvut.sort()
sortattu = luvut[-5:]
for i in sortattu:
    print(i)