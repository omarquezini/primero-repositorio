import random

fruta = ["maçã", "banana", "laranja", "uva", "manga" ]

print("lista de frutas: ")

for i in range (len(fruta)):
    print (f"{i + 1} - {fruta[i]}")

posicao_sorteada = random.randint(1,5)

palpite = input("Qual fruta você acha que está na posição sorteada? ")

fruta_certa = fruta[posicao_sorteada - 1]

if palpite.capitalize() == fruta_certa:
    print("parabens! você acertou!")
    print(f"A fruta da posição {posicao_sorteada} era realmente {fruta_certa}. ")
else:
    print("ERROU!")
    print(f"A fruta da posição {posicao_sorteada} era {fruta_certa} seu burro. ")