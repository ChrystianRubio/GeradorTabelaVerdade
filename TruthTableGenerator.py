import re
import csv
import os


class myStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def size(self):
        return len(self.stack)

    def empty(self):
        return self.size() == 0

    def top(self):
        return self.stack[-1]

    def pop(self):
        res = self.top()
        self.stack.pop()
        return res


def Priority(c: str):
    """'retornando ordem de prioridade dos operadores"""
    if (c == '('):
        return 0
    elif (c == '>' or c == '~'):
        return 1
    elif (c == 'v' or c == '^'):
        return 2
    else:
        assert (c == '!')
        return 3


def Oper(x: int, y: int, oper: str):
    """Calculando expressões(x operador y), com 'operador' sendo [v,^,<->,->]"""
    if (oper == 'v'):
        return (x | y)  # x v y
    elif (oper == '^'):
        return (x & y)  # x ^ y
    elif (oper == '>'):
        return ((1 ^ y) | x)  # x -> y
    else:
        assert (oper == '~')
        return (1 if (x == y) else 0)  # x <-> y


def preprocess(expression: str):
    expression = re.sub(' ', '', expression)  # deleta todo o espaço
    # para uma programação fácil, Eu converti todos os operadores multi-caracteres para um caractere único
    expression = re.sub('<->', '~', expression)
    expression = re.sub('->', '>', expression)
    # - e ! ambos são representantes para o operador NOT(negação)
    expression = re.sub('-', '!', expression)
    # + e v ambos são representantes para o operador OR(ou)
    expression = re.sub('\+', 'v', expression)
    # . e ^ ambos são representantes para o operador AND(e)
    expression = re.sub('\.', '^', expression)
    # !! é um operador que apaga tudo
    while (re.search('!!', expression) != None):
        expression = re.sub('!!', '', expression)
    return expression


def GetVariable(expression: str):
    """Obtém todas as variáveis que apareceram em 'expression'"""
    SetVar = set()
    ListVar = []
    for c in expression:
        if ('a' <= c) and (c <= 'z') and (c != 'v'):  # v é um operador
            if (c in SetVar):
                continue
            SetVar.add(c)
            ListVar.append(c)
    return ListVar


def GetRPN(expression: str):
    """Usando shunting-yard algorithm(algoritmo de desvio de jardas) para 
    obter Reverse Polish notation(Notação polonesa inversa) da 'expression' 
    da notação Infix"""
    stack = myStack()
    RPN = myStack()
    for c in expression:
        if c == '(':
            stack.push(c)
        elif c == ')':
            while True:
                x = stack.pop()
                if (x != '('):
                    RPN.push(x)
                else:
                    break
        elif c in ['v', '^', '>', '~', '!']:
            while (not stack.empty()) and Priority(c) <= Priority(stack.top()):
                RPN.push(stack.pop())
            stack.push(c)
        elif (c == '0' or c == '1' or (('a' <= c) and (c <= 'z') and (c != 'v'))):
            RPN.push(c)
    while (not stack.empty()):
        RPN.push(stack.pop())
    return RPN


def Calculate(RPN: myStack, VariableValue: dict):
    """Calcula o valor da expressão da RPN, com valor da variável armazenada em 'VariableValue'"""
    res = myStack()
    for c in RPN.stack:
        if (c == '0' or c == '1' or (('a' <= c) and (c <= 'z') and (c != 'v'))):  # 'v' é um operador
            res.push(VariableValue[c])
        elif (c == '!'):
            res.push(1 ^ res.pop())  # not X, !X, -X
        else:
            assert (c == '^' or c == 'v' or c == '>' or c == '~')
            x = res.pop()
            y = res.pop()
            res.push(Oper(x, y, c))
    assert (res.size() == 1)
    return res.pop()


def WriteToConsole(result: list):
    for row in result:
        tmp = row.pop()
        for x in row:
            print("  ", x, end="  |", sep='')
        print("  ", tmp, sep='')
        row.append(tmp)

# Cria um arquivo ou subscreve um já existente
def WriteToFile(result: list):
    nomearqv = ""
    while (True):
        if nomearqv == "":
            nomearqv = input('Insira o nome do arquivo: ')
            if not os.path.isfile(nomearqv):
                csvFile = open(nomearqv, 'w')
                writer = csv.writer(csvFile)
                writer.writerows(result)
                csvFile.close()
                break
        else:
            subscrever = input(
                'O arquivo já existe! Deseja subscrever?\n1 - Sim\n2 - Não\n Informe a opção desejada: ')
            if subscrever == '1':
                csvFile = open(nomearqv, 'w')
                writer = csv.writer(csvFile)
                writer.writerows(result)
                csvFile.close()
                break
            elif subscrever == '2':
                nomearqv = ""
            elif subscrever != '1' and subscrever != '2':
                print('Opção inválida! Insira uma opção válida.')


def Solve(expression: str):
    """ Função que representa a solução de todo o código,
        ela que será chamada na main para executar as demais funções"""
    result = []

    ListVariable = GetVariable(expression)
    ListVariable.append(expression)
    result.append(ListVariable.copy())
    ListVariable.pop()

    expression = preprocess(expression)
    RPN = GetRPN(expression)
    n = len(ListVariable)

    # Força todos os valores de todas as variáveis
    for mask in range(2 ** n):
        VariableValue = {'0': 0, '1': 1}
        cur = []
        for i in range(n):
            VariableValue[ListVariable[i]] = (mask >> (n - i - 1) & 1)
            cur.append(mask >> (n - i - 1) & 1)
        cur.append(Calculate(RPN, VariableValue))
        result.append(cur)
    # Escreve no console o resultado(result)
    while (True):
        WriteToConsole(result)
        save = input(
            "Deseja salvar este resultado?\n 1 - Sim\n 2 - Não\n Informe sua escolha: ")
        if save == '1':
            WriteToFile(result)
            print('\nArquivo salvo com sucesso!')
            break
        elif save == '2':
            print('\nOk, não salvamos seu resultado.')
            break
        else:
            os.system('clear') or None
            print('Opção selecionada é inválida!\nPor favor, insira uma opção válida.')


def main():
    expression = input("Por favor atente-se que sua expressão deve usar apenas letras minúsculas para representar variáveis, mas não use 'v' como variável, pois ele é um operador."
                       " Utilize parênteses para priorizar determinada operação.\n"+"Abaixo está a lista com os operadores disponíveis.\n\n"
                        "  Negação: indicado como '!' ou '-'        \n"
                        "  Conjunção: denotado como '^' ou '.'      \n"
                        "  Disjunção: denotado como 'v' ou '+'      \n"
                        "  Condicional: indicada como '->' ou '>'   \n"
                        "  Bicondicional: denotado como '<->' ou '~'\n\n"  
                       "Escreva a sua sentença: ")
    Solve(expression)


if __name__ == '__main__':
    main()
