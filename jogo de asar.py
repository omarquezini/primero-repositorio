import random

numero_aleatorio = random.randint(1, 9)

acertou = False

while not acertou:
    try:
        numero_digitado = int(input("Digite um número entre 1 e 9: "))
        
        if numero_digitado < 1 or numero_digitado > 10:
            print("Por favor, digite um número entre 1 e 9.")
            continue

        elif numero_digitado == numero_aleatorio:
            print("Você venceu!")
            acertou = True
        else:
            print("Você errou. Tente novamente.")
    except ValueError:
        print("apenas números! idiota.")