from functions.funcoes import add, sub, mult, div
from time import sleep

title = 'CALCULADORA'

print('-=' * 20)
print(f'{title:^40}')
print('-=' * 20)

while True:
    print('Escolha uma das opções a seguir:')
    print('''1 - Soma | 2 - Subtração | 3 - Multiplicação | 4 - Divisão | 5 - Sair\n''')

    opcao = int(input('Operação: '))
    print('-=' * 20)

    while opcao == 1:
        num1 = float(input('Primeiro Número: '))
        num2 = float(input('Segundo Número: '))
        print()

        print(f'Resultado: {num1} + {num2} =', add(num1, num2))
        pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
        print('-=' * 20)

        if pergunta == 'S':
            continue
        else:
            break

    while opcao == 2:
        num1 = float(input('Primeiro Número: '))
        num2 = float(input('Segundo Número: '))
        print()

        print(f'Resultado: {num1} - {num2} =', sub(num1, num2))
        pergunta = str(input('Deseja Continuar? [S/N] ')).strip().upper()
        print('-=' * 20)

        if pergunta == 'S':
            continue
        else:
            break

    while opcao == 3:
        num1 = float(input('Primeiro Número: '))
        num2 = float(input('Segundo Número: '))
        print()

        print(f'Resultado: {num1} * {num2} =', mult(num1, num2))
        pergunta = str(input('Deseja Continuar? [S/N] ')).strip().upper()
        print('-=' * 20)

        if pergunta == 'S':
            continue
        else:
            break

    while opcao == 4:
        num1 = float(input('Primeiro Número: '))
        num2 = float(input('Segundo Número: '))
        print()

        print(f'Resultado: {num1} / {num2} =', div(num1, num2))
        pergunta = str(input('Deseja Continuar? [S/N] ')).strip().upper()
        print('-=' * 20)

        if pergunta == 'S':
            continue
        else:
            break

    if opcao == 5:
        pergunta = str(input('Deseja Sair Da Calculadora? [S/N] ')).strip().upper()

        if pergunta == 'S':
            print('ENCERRANDO CALCULADORA...')
            sleep(2)
            print('CALCULADORA ENCERRADA COM SUCESSO!')
            break
        else:
            continue
