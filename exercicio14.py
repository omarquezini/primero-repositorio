salario = int(input("Digite seu salário mensal. "))
parcela = int(input("Digite o valor da parcela. "))

limite = salario * 0.35

print(f"Limite máximo da parcela: R${limite:.2f}")

if salario > 3000 and parcela <= limite:
    print("Financiamento aprovado. ")
else:
    print("Financiamento negado. ")