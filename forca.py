def jogar():
    print("*****************************")
    print("Bem vindo ao jogo de Forca!!!")
    print("*****************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    enforcado = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    
    while(not enforcado and not acertou):
        chute = input("Digite uma letra: ").strip().lower()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcado = erros == 6
        acertou = "_" not in letras_acertadas     
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!!!")
    else:
        print("Você perdeu!!!")           

if(__name__ == "__main__"):
    jogar()