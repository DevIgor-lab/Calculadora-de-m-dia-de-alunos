# Como automatizar a média dos alunos
# Primeiro realize a estrutura que deseja obter para inserção dos dados.

# Insira o nome do Aluno.
print("Bem-vindos ao Software do Colégio Educa Python\n")
print("Nesse sistema iremos Calcular a Média das Notas das provas realizadas, verificar os Aprovados e Reprovados juntamente com a necessidade da realização da Prova de Recuperação dos Alunos!\n")

# Insira o nome do Aluno.
nome1 = input("Digite o nome do Aluno:")
nome2 = input("Digite o nome do Aluno:")
print()

print("Relação de Alunos que realizaram as provas:\n")
print("Aluno:", nome1)

print("Aluno:", nome2)
print()

# Mensagem de inserção de notas do Aluno para realização da Média.
print("Digite as notas das provas realizadas pelos Alunos:\n")

# Insira as notas para o primeiro Aluno.
Nota_1 = int(input(f"Digite a primeira nota para {nome1}:"))
Nota_2 = int(input(f"Digite a segunda nota para {nome1}:"))
Nota_3 = int(input(f"Digite a terceira nota para {nome1}:"))
Nota_4 = int(input(f"Digite a quarta nota para {nome1}:"))
print()
# Insira as notas para o segundo Aluno.
Nota_5 = int(input(f"Digite a primeira nota para {nome2}:"))
Nota_6 = int(input(f"Digite a segunda nota para {nome2}:"))
Nota_7 = int(input(f"Digite a terceira nota para {nome2}:"))
Nota_8 = int(input(f"Digite a quarta nota para {nome2}:"))
print()
# A partir das notas inseridas, calcule a média do Aluno.
media1 = (Nota_1+Nota_2+Nota_3+Nota_4)/4
media2 = (Nota_5+Nota_6+Nota_7+Nota_8)/4

if media1 >= 6:
  situacao1 = "Aprovado"
else:
  situacao1 = "Reprovado"

if media2 >= 6:
  situacao2 = "Aprovado"
else:
  situacao2 = "Reprovado"

# Verificar a média, situação e possível recuperação dos Alunos.
print(f"A media das notas é: {media1}")
print(f"Situação do(a) {nome1}: {situacao1}")
situacao1 = "Sim" if media1 <= 6 else "Não"
print(f"Realizar recuperação:", situacao1)
print()
print(f"A media das notas é: {media2}")
print(f"Situação do(a) {nome2}: {situacao2}")
situacao2 = "Sim" if media2 <= 6 else "Não"
print(f"Realizar recuperação:", situacao2)
print()