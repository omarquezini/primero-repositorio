alunos =["alice","bruno","carla"]

dias = [["ausente" for _ in dias] for _ in alunos]

print ("preencha com 's'para presença e 'x' para ausencia")

for i, aluno in enumerate(alunos):
    print(f"\nAluno: {aluno}")
    for j, dia in enumerate(dias):
        entrada = input(f" {dias}: ")
        if entrada.upper() == 's':
            reserva[i][j] = "presente"

print("\nTabela de reservas:")
print(f"{'Aluno':<10} {' '.join([f'{d:<10}'for d in dias])}")
for i, aluno in enumerate(alunos):
    print(f"{aluno:<10} {' '.join([f'{res:<10}' for res in reserva[i]])}")