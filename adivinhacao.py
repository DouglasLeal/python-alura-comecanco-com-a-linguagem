print("***********************************")
print("Bem vindo ao jogo da Adivinhação!!!")
print("***********************************")

numero_secreto = 42

chute = int(input("Digite o seu número: "))

print(f"Você digitou: {chute}")

if(numero_secreto == chute):
    print("Você acertou")
elif(numero_secreto < chute):
    print("Errado! Seu chute foi maior que o número secreto.")
else:
    print("Errado! Seu chute foi menor que o número secreto.")

print("Fim do Jogo!!!")