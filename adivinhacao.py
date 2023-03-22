import random

print("***********************************")
print("Bem vindo ao jogo da Adivinhação!!!")
print("***********************************")

numero_secreto = random.randrange(1, 101)
total_tentativas = 10
rodada_atual = 1

print("Qual o nível de dificuldade?")
print("(1) Fácil | (2) Médio | (3) Difícil")
nivel = int(input("Escolha o nível: "))

if(nivel == 1):
    total_tentativas = 20
elif(nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5

while(rodada_atual <= total_tentativas):
    print(f"Tentativa {rodada_atual} de {total_tentativas}")

    chute = int(input("Digite um número de 1 a 100: "))

    print(f"Você digitou: {chute}")

    if(chute < 1 or chute > 100):
        print("Valor inválido!")
        continue

    if(numero_secreto == chute):
        print("Você acertou!!!")
        break
    elif(numero_secreto < chute):
        print("Errado! Seu chute foi maior que o número secreto.")
    else:
        print("Errado! Seu chute foi menor que o número secreto.")

    rodada_atual += 1

print("Fim do Jogo.")