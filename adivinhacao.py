def jogar_adivinhacao():
    from ast import While
    import random

    print ("========================")
    print("Bem vindo ao jogo")
    print ("========================")

    numero_secreto = random.randrange(1,51)
    tentativas = 0
    pontos = 1000

    print("Qual a dificuldade meu nobre?")
    print("(1)Fácil (2)Média (3)Hardcore")
    nivel = int(input("A escolhida foi? "))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    #while recebe condição e executa todas as vezes que a condição for verdadeira 
    for rodada in range (1, tentativas + 1):
        chute_str = input("Digite o seu número de 1 a 50: ")
        print("Tentativas {} de {}".format (rodada, tentativas))
        print("Você digitou: ", chute_str)
        chute = int(chute_str)
        
        if (chute < 1 or chute > 50):
            print("Você deve digitar somente entre 1 e 50!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Você acertou! Sua pontuação foi {}" .format (pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar_adivinhacao()                    