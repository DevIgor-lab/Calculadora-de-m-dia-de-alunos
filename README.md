# Sistema de Média Escolar

## Descrição

Este projeto é um script em Python que simula um sistema simples de controle escolar. O programa coleta os nomes de dois alunos, recebe quatro notas para cada um, calcula a média final e informa:

* Situação do aluno (**Aprovado** ou **Reprovado**)
* Necessidade de **Recuperação**

O objetivo do projeto é praticar conceitos básicos de programação com Python, como:

* Entrada de dados (`input`)
* Saída de dados (`print`)
* Variáveis
* Operações matemáticas
* Estruturas condicionais (`if` / `else`)

---

## Arquivo do Projeto

* `Sistema.py` → código principal do sistema.

---

## Como Executar

### Pré-requisitos

* Python 3 instalado.

### Passos

1. Baixe o arquivo `Sistema.py`.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:

```bash
python Sistema.py
```

---

## Funcionamento

1. O sistema solicita o nome de dois alunos.
2. Solicita quatro notas para cada aluno.
3. Calcula a média de cada aluno:

```python
media = (nota1 + nota2 + nota3 + nota4) / 4
```

4. Define a situação:

* Média maior ou igual a `6` → **Aprovado**
* Média menor que `6` → **Reprovado**

5. Define recuperação:

* Média menor ou igual a `6` → **Sim**
* Média maior que `6` → **Não**

---

## Exemplo de Uso

```text
Digite o nome do Aluno: João
Digite o nome do Aluno: Maria

Digite a primeira nota para João: 8
Digite a segunda nota para João: 7
Digite a terceira nota para João: 9
Digite a quarta nota para João: 6
```

Saída esperada:

```text
A media das notas é: 7.5
Situação do(a) João: Aprovado
Realizar recuperação: Não
```

---

## Melhorias Futuras

Sugestões para evolução do projeto:

* Permitir cadastrar mais de dois alunos
* Usar listas e laços de repetição
* Validar notas entre 0 e 10
* Melhorar organização com funções
* Exportar resultados para arquivo `.txt` ou `.csv`
* Criar interface gráfica

---

## Autor

Projeto desenvolvido para fins de estudo em Python.
