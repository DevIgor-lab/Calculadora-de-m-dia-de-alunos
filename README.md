# README - Sistema de Cadastro e Média Escolar em Python

## 📌 Descrição

Este projeto em Python foi desenvolvido para fins educacionais e demonstra conceitos básicos de programação, como:

* Exibição de mensagens na tela
* Uso de variáveis
* Entrada de dados com `input()`
* Cálculo de média aritmética
* Estruturas condicionais (`if/else`)
* Saída formatada com `f-string`

O programa solicita o nome do usuário, dá uma mensagem de boas-vindas e depois pede quatro notas para calcular a média final do aluno, informando se ele foi **Aprovado** ou **Reprovado**.

---

## 🚀 Funcionalidades

✅ Exibe mensagem `Hello, World`
✅ Solicita nome do usuário
✅ Exibe saudação personalizada
✅ Solicita 4 notas
✅ Calcula média final
✅ Informa situação do aluno

---

## 🧾 Código

```python
print("Hello, World\n")

x = 10
nome = 'Aluno'
nota = 8.75
fez_inscrição = True

nome = input("Digite um nome:\n")

print(f"\nOlá {nome}, bem-vindo a disciplina de programação. Parabéns pelo seu primeiro Hello World!\n")

Nota_1 = int(input("Digite a primeira nota:"))
Nota_2 = int(input("Digite a segunda nota:"))
Nota_3 = int(input("Digite a terceira nota:"))
Nota_4 = int(input("Digite a quarta nota:"))

media = (Nota_1 + Nota_2 + Nota_3 + Nota_4) / 4

if media >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print(f"\nA média das notas é: {media}")
print(f"Situação do aluno: {situacao}")
```

---

## ▶️ Como Executar

### 1. Instale o Python

Baixe e instale o Python no site oficial:

https://www.python.org/

### 2. Salve o arquivo

Exemplo:

```bash
programa.py
```

### 3. Execute no terminal

```bash
python programa.py
```

---

## 💻 Exemplo de Uso

```text
Hello, World

Digite um nome:
Maria

Olá Maria, bem-vindo a disciplina de programação.

Digite a primeira nota: 8
Digite a segunda nota: 7
Digite a terceira nota: 9
Digite a quarta nota: 6

A média das notas é: 7.5
Situação do aluno: Aprovado
```

---

## 📚 Conceitos Aplicados

* Variáveis e tipos de dados
* Entrada e saída de dados
* Conversão com `int()`
* Operações matemáticas
* Estrutura condicional
* Formatação de strings

---

## 🔧 Melhorias Futuras

* Permitir notas decimais (`float`)
* Validar notas entre 0 e 10
* Repetir cadastro para vários alunos
* Interface gráfica
* Armazenamento em arquivo

---

## 👨‍💻 Autor

Projeto desenvolvido para estudos em lógica de programação com Python.
