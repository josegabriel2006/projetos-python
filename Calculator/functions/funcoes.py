# FUNÇÕES DAS OPERAÇÕES
def add(num1, num2):
    resulado = num1 + num2
    return resulado

def sub(num1, num2):
    resultado = num1 - num2
    return resultado

def mult(num1, num2):
    resultado = num1 * num2
    return resultado

def div(num1, num2):
    if num2 == 0:
        return 'Não é possível dividir um número por 0!'
    else:
        resultado = num1 / num2
        return resultado