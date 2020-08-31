import random 

def jogar():

    print("********************************")
    print("Bem Vindo ao Jogo de Advinhação!")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade quer jogar?")
    print("(1) Facíl, (2) Médio, (3) Difícil")

    nivel = int(input("Define o nível:"))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        
        chute = int(input("Digite um número de 1 a 100: "))
        print("Você digitou", chute)
        
        if(chute < 1 or chute > 100):
            print("Você deve informar um número entre 1 e 100!")
            continue

        acertou =  chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você Acertou! Sua pontuação foi {} pontos!!".format(pontos))
            break
        else:
            if(maior):
                print("Voce Errou! O seu número foi maior do que o número secreto")
            elif(menor):
                print("Voce Errou! O seu número foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo.")