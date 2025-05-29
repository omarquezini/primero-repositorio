umidade = int(input("digite o porcentual da umidade. "))

if umidade >= (70 / 100)*100 :
    print("A UMIDADE UTRAPASSOU 70%. ")
else:
    print(f"umidade dentro do padrao:{umidade}%.")
    