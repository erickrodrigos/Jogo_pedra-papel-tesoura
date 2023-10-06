#DESAFIO DE PEDRA PAPEL E TESOURA ONDE DEVE SER PEDIDO A CADA UM DOS JOGADORES (E NO CASO)
#QUAL OPÇÃO QUEREM:
# 1 = PEDRA : 2 = PAPEL : 3 = TESOSURA
jogador1 = 1
jogador2 = 1
contT = 0

while True:
    while contT != 3:
        jogador1 = int(input("   Desafio do PPT\n 1 = PEDRA\n  2 = PAPEL\n  3 = TESOSURA\n informe o que deseja:   "))
        if (jogador1 < 0 or jogador1 > 3 ):
            print("Opções incorretas!!!")
            contT+= 1
        else:
             contT = 0
             break
    if contT == 3:
        print("            TENTATIVAS ENCERRADAS!!!")
        break

    while contT != 3:
        jogador2 = int(input("   Jogador 2 \n 1 = PEDRA\n  2 = PAPEL\n  3 = TESOSURA\n informe o que deseja:   "))
        if (jogador2 < 0 or jogador2 > 3 ):
            print("Opções incorretas!!!")
            contT+= 1
        else:
             break
    if contT == 3:
        print("            TENTATIVAS ENCERRADAS!!!")
        break
    # se o jogador 1 escolher papel e o 1 pedra ou escolher pedra e 0 1 tesoura
    if jogador1 != jogador2:
        if (jogador1 - jogador2 == 1) or (jogador1 - jogador2 == -2):
                print("jogador 1 venceu !!!!!!!")
        else:
            print("Jogador 2 venceu !!!!!")
    else:
        print("são iguais EMPATE!!!")
    repetir = input("Deseja continuar ? digite 1 se sim, caso não digite qualquer tecla ")
    if repetir != '1':
        break
print("")
print("                 FIM DE JOGO !!!!")