import forca
import adivinhacao

def escolha_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca")
    print("(2) Adivinhação")

    jogo = input("Qual jogo?")

    match jogo:
        case "1":
            print("Jogando Forca!")
            forca.jogar()
        case "2":
            print("Jogando Adivinhação!")
            adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()

