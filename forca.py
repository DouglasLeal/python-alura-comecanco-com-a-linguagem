def jogar():
    print("*****************************")
    print("Bem vindo ao jogo de Forca!!!")
    print("*****************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    enforcado = False
    acertou = False

    print(letras_acertadas)
    
    while(not enforcado and not acertou):
        chute = input("Digite uma letra: ").strip().lower()

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
            index += 1

        print(letras_acertadas)
                

if(__name__ == "__main__"):
    jogar()