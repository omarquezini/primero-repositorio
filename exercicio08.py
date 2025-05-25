distancia = int(input("digite o numero da distancia Km. "))

tempo = int(input("digite o numero do tempo h. "))

velocidade = (distancia / tempo)

if velocidade < 5:
    print("você foi lento. ")
elif velocidade == 5 or velocidade == 10:
    print("você foi moderado em sua velocidade. ")
elif velocidade > 10:
    print("você foi rapido")