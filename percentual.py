#Dados do faturamento
SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
TOTAL = 160910.45
opcao = 0
while opcao != 5:
    print('''   [ 1 ] SP R$67.836,43
          [ 2 ] RJ R$36.678,66
          [ 3 ] MG R$29.229,88
          [ 4 ] ES R$27.165,48
          [ 5 ] SAIR ''')
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        SP = (SP/TOTAL)*100
        print(str('Valor é {:.1f}'.format(SP) + ' %'))
    elif opcao == 2:
        RJ = (RJ/TOTAL)*100
        print(str('Valor é {:.1f}'.format(RJ) + ' %'))
    elif opcao == 3:
        MG = (MG/TOTAL)*100
        print(str('Valor é {:.1f}'.format(MG) + ' %'))
    elif opcao == 4:
        ES = (ES/TOTAL)*100
        print(str('Valor é {:.1f}'.format(ES) + ' %'))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida tente novamente!!!')
