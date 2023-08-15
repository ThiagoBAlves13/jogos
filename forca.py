def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "desenvolvimento"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print(f'Encontrei a letra {chute} na posição {index}')
            index +=1
        print("jogando ...")

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()