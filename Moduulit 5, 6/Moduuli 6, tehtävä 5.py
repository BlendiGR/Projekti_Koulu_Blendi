randomi_lista = [58, 44, 30, 21, 17, 16, 60, 6, 63, 18, 46, 26, 83, 39, 42, 95, 99, 25, 83, 49, 63, 5, 30, 65, 28]

def parittomien_lukujen_poistaja(lista):
    list = []
    for i in lista:
        if i % 2 == 0:
            list.append(i)
    return list

print(f" Uusi lista : {parittomien_lukujen_poistaja(randomi_lista)} \n Vanha lista : {randomi_lista}")
