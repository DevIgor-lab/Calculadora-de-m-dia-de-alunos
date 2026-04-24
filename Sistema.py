print("Olá, Mundo\n")

x = 10
nome = 'Aluno'
nota = 8.75
fez_inscrição = True

nome = input("Digite um nome:\n")

print(f"\nÓla {nome}, bem-vindo a disciplina de programação. Parabéns pelo seu primeiro Hello World!\n")

Nota_1 = int(input("Digite a primeira nota:"))
Nota_2 = int(input("Digite a segunda nota:"))
Nota_3 = int(input("Digite a terceira nota:"))
Nota_4 = int(input("Digite a quarta nota:"))

media = (Nota_1+Nota_2+Nota_3+Nota_4)/4

if media >= 6:
  situacao = "Aprovado\n"
else:
  situacao = "Reprovado\n"

print(f"\nA media das notas é: {media}\n")
print(f"Situação do aluno: {situacao}\n")