horaAtual = int(input("Digite a hora atual (formato 24h): "))

if 9 <= horaAtual <= 21:
    print("Acesso permitido. ")
else:
    print("Acesso negado. ")