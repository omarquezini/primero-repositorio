distancia = int(input("digite o valor da distancia."))

if distancia <=50:
    print("$5,00")
elif 51 <= distancia <= 150:
    print("$15,00")
elif distancia > 150:
    print("$25,00")