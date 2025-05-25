intregaX = int(input("digite o tempo restante da intragaX. "))
intregaY = int(input("digite o tempo restante da intragaY. "))
intregaZ = int(input("digite o tempo restante da entregaZ. "))

if intregaX >= 0 or intregaY >= 0 or intregaZ >= 0:
    print(intregaX+intregaY+intregaZ)
elif intregaX < 0 or intregaY < 0 or intregaZ < 0:
    print("ERRO")