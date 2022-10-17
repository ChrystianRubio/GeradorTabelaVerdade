# Truth Table Generator
This python code is auto generate truth table of  a Logical Epression (LE), such as (p v (p ^ q)) ^ !p -> r. 

# Supported Operations

Has support to 5 operators: 
- NOT: denoted as '!' or '-' . 
- AND: denoted as '^' or '.' .
- OR: denoted as 'v' or '+' .
- Material Implication: denoted as '->' or '>' .
- equivalence: denoted as '<->' or '~' .

**Order of operations**: NOT > AND = OR > Material Implication = Equivalence
- The NOT operators will calculate first (highest priority).
- Then, the AND and OR operators.
- Last, the Material Implication and equivalence (lowest priority).
- It will calculate from left to right if 2 operators have the same order.

# How to use
Download [TruthTableGenerator.py](TruthTableGenerator.py) and run by command `python TruthTableGenerator.py`, then enter your logical expression, it will output a Truth Table of your LE.

You can use lower letter to represent variables, but don't use 'v' as variable, because it is an operator in my code. Therefore, you can use at most 25 variables. But my time complexity is about O(2^n) with a ton of constants, so you shouldn't use too much variables, less than 15 variables is fine.

# Example
My expression is: (p v (p ^ q)) ^ !p -> r

This is the generated truth table:
```
  p  |  q  |  r  |  (p v (p ^ q)) ^ !p -> r
  0  |  0  |  0  |  1
  0  |  0  |  1  |  1
  0  |  1  |  0  |  1
  0  |  1  |  1  |  1
  1  |  0  |  0  |  1
  1  |  0  |  1  |  1
  1  |  1  |  0  |  1
  1  |  1  |  1  |  1
```

# Português


# Gerador de tabela verdade
Este código em python é um gerador automático de tabela verdade de uma expressão Lógica (LE), como (p v (p ^ q)) ^ !p -> r.

# Operações suportadas

Tem suporte a 5 operadores:
- NOT: indicado como '!' ou '-' .
- AND: denotado como '^' ou '.' .
- OR: denotado como 'v' ou '+' .
- Implicação material: indicada como '->' ou '>' .
- equivalência: denotado como '<->' ou '~' .

**Ordem das operações**: NOT > AND = OR > Implicação do Material = Equivalência
- Os operadores NOT calcularão primeiro (prioridade mais alta).
- Em seguida, os operadores AND e OR.
- Por último, a Implicação Material e equivalência (menor prioridade).
- Calculará da esquerda para a direita se 2 operadores tiverem o mesmo pedido.

# Como usar
Faça o download do [TruthTableGenerator.py](TruthTableGenerator.py) e execute o comando `python TruthTableGenerator.py`, depois insira sua expressão lógica, ele produzirá uma Tabela Verdade do seu LE.

Você pode usar letra minúscula para representar variáveis, mas não use 'v' como variável, pois é um operador neste código. Portanto, você pode usar no máximo 25 variáveis.

# Exemplo
Minha expressão é: (p v (p ^ q)) ^ !p -> r

Esta é a tabela verdade gerada:
```
  p | q | r | (p v (p ^ q)) ^ !p -> r
  0 | 0 | 0 | 1
  0 | 0 | 1 | 1
  0 | 1 | 0 | 1
  0 | 1 | 1 | 1
  1 | 0 | 0 | 1
  1 | 0 | 1 | 1
  1 | 1 | 0 | 1
  1 | 1 | 1 | 1
```

