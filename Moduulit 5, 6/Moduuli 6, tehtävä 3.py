def gallon_to_litre(inputti):
    return inputti * 3.78541178


while True:
    try:
        inputti = float(input("Anna galloonat : "))
        if inputti < 0:
            break
        print(gallon_to_litre(inputti))
    except ValueError:
        print("Anna kelvollinen numero")
        break

