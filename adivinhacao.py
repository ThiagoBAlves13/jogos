import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    total_de_tentativas = 0
    numero_secreto = random.randrange(1,101) #round(random.random())) #0.0 a 1.0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil, (2) Médio, (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5
    #rodada = 1

    #while(rodada <= total_de_tentativas):
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativas {} de {}!".format(rodada,total_de_tentativas))
        chute = int(input("Digite o seu número: "))
        if(chute < 1 or chute > 100):
            print("Digite um número entre 1 e 100!")
            continue
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu número foi maior.")
            elif(menor):
                print("Você errou! O seu número foi menor.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        if(rodada == total_de_tentativas):
            print("O número secreto era {}. Você fez {} pontos".format(numero_secreto,pontos))
        print("Pontuação atual: ", pontos)
     #   rodada = rodada + 1
    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()