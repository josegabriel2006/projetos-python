from time import sleep

nome_sistema = 'NEXUS SYSTEM'
print('\033[1m-=' * 30)
print(f'{nome_sistema:^60}')
print('-=' * 30)

while True:
    print('[1] CALCULAR IMC')
    print('[2] CALCULAR DESCONTO DE COMPRA')
    print('[3] CLASSIFICAÇÃO ETÁRIA DE FILME')
    print('[4] CALCULADORA')
    print('[5] SAIR DO SISTEMA')

    opcao = int(input('Opção: '))

    print('-=' * 30)

    # CALCULA O IMC
    while opcao == 1:
        print('CALCULAR IMC')
        peso = float(input('Digite seu Peso: '))
        altura = float(input('Sua Altura: '))
        imc = peso / pow(altura, 2)
        print(f'Seu IMC é de = {imc:.1f}Kg')

        if imc < 18.5:
            print('Classificação: ABAIXO DO PESO!')
        elif 18.5 <= imc < 25:
            print('Classificação: PESO NORMAL!')
        elif 25 <= imc < 30:
            print('Classificação: SOBREPESO!')
        elif 30 <= imc < 35:
            print('Classifiacação: OBESIDADE GRAU I!')
        elif 35 <= imc < 40:
            print('Classifiacação: OBESIDADE GRAU II!')
        else:
            print('Classifiacação: OBESIDADE GRAU III!')

        # PERGUNTA SE O USUÁRIO QUER CONTINUAR
        escolha = str(input('Deseja continuar (s/n)? '))

        # VERIFICA SE O USUÁRIO DIGITOU S/N
        if escolha == 's':
            continue
        else:
            break

    # CALCULAR O DESCONTO DE UMA COMPRA
    while opcao == 2:
        print('CALCULAR DESCONTO DE UMA COMPRA')
        preco_original = float(input('Digite o Valor do Produto: '))
        desconto = int(input('Desconto (10% ou 15%): '))

        if desconto == 10:
            valor_desconto = preco_original * (desconto / 100)
            valor_final = preco_original - valor_desconto
            print(f'Preço Final: R${valor_final:.2f}')
        elif desconto == 15:
            valor_desconto = preco_original * (desconto / 100)
            valor_final = preco_original - valor_desconto
            print(f'Preço Final: R${valor_final:.2f}')
        else:
            print('DESCONTO INVÁLIDO! TENTE UM DESCONTO DE 10% OU 15%')

        # PERGUNTA SE O USUÁRIO QUER CONTINUAR
        escolha = str(input('Deseja continuar (s/n)? '))
        print()

        # VERIFICA SE O USUÁRIO DIGITOU S/N
        if escolha == 's':
            continue
        else:
            break

    # CLASSIFICAÇÃO ETÁRIA DE FILME
    while opcao == 3:
        print('CLASSIFICAÇÃO ETÁRIA DE FILMES')
        idade = int(input('Digite sua Idade: '))
        if idade < 12:
            print('Este filme é LIVRE para todos os públicos')
        elif (idade >= 12) and (idade <= 15):
            print('Este filme é recomendado para maiores de 12 Anos')
        elif (idade >= 16) and (idade <= 17):
            print('Este filme é recomendado para maiores de 16 Anos')
        else:
            print('Este filme é recomendado para maiores de 18 anos')

        # PERGUNTA SE O USUÁRIO QUER CONTINUAR
        escolha = str(input('Deseja continuar (s/n)? '))
        print()

        # VERIFICA SE O USUÁRIO DIGITOU S/N
        if escolha == 's':
            continue
        else:
            break

    # CALCULADORA
    if opcao == 4:
        while True:
            print('CALCULADORA')
            print('[1] SOMA')
            print('[2] MULTIPLICAÇÃO')
            print('[3] DIVISÃO')
            print('[4] POTENCIAÇÃO')
            opcao_calculadora = int(input('Escolha Operação: '))

            # VERIFICA AS OPÇÕES
            if opcao_calculadora == 1:
                num1 = int(input('Primeiro Número: '))
                num2 = int(input('Segundo Número: '))
                soma = num1 + num2
                print(f'SOMA: {num1} + {num2} = {soma}')

            if opcao_calculadora == 2:
                num1 = int(input('Primeiro Número: '))
                num2 = int(input('Segundo Número: '))
                mult = num1 * num2
                print(f'MULTIPLICAÇÃO: {num1} * {num2} = {mult}')

            if opcao_calculadora == 3:
                num1 = int(input('Primeiro Número: '))
                num2 = int(input('Segundo Número: '))

                # VERIFICA SE É DIVISIVEL POR 0
                if num2 == 0:
                    print('NÃO EXISTE DIVISÃO POR 0!')
                else:
                    div = num1 / num2
                    print(f'DIVISÃO: {num1} / {num2} = {div}')

            if opcao_calculadora == 4:
                num1 = int(input('Número: '))
                num2 = int(input('Expoente: '))
                pot = pow(num1, num2)
                print(f'POTÊNCIA: {num1} elevado há {num2} = {pot}')

            # PERGUNTA SE O USUÁRIO QUERO CONTINUAR NA CALCULADORA
            escolha = str(input('Deseja continuar (s/n)? '))
            print()

            # VERIFICA SE O USUÁRIO DIGITOU S/N
            if escolha == 's':
                continue
            else:
                break

    # SAIR DO SISTEMA
    if opcao == 5:
        print('ENCERRANDO O SISTEMA...')
        sleep(2)
        print('SISTEMA ENCERRADO COM SUCESSO!')
        break

    # VERIFICA SE A OPÇÃO É DIFERENTE DE 4
    if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE\033[1m')

    print('-=' * 30)