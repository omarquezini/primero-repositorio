curso02 = int(input("digite a quantidadede de avaliaçoes desse curso02. "))

curso01 = int(input("digite a quantidade de avaliaçoes desse curso01. "))

if curso01 == curso02:
    print("empate, A É.")
elif curso02 > curso01:
    print("cursso02 teve mais avaliaçoes.")
else:
    print("o curso01 teve mais avaliaçoes.")

