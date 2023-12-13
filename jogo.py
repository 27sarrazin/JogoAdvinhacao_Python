import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhacao!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_tentativas = 0
pontos = 1000

print("qual nivel de dificuldade?")
print("(1) Facil (2) Medio (3) Dificil")
print(numero_secreto)

nivel = int(input("define o nivel: "))

if(nivel == 1):
    total_tentativas = 20
elif (nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5


for rodada in range(1, total_tentativas + 1):
    print(f"tentativa:  {rodada} de {total_tentativas}")
    chute_str = input("Digite um numero entre 1 e 100: ")
    print("Voce digitou: ", chute_str)
#Convertendo uma string para numero inteiro
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("voce deve digitar um numero entre 1 e 100")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print(f"Voce acertou e fez {pontos}!")
        break
    else:
        if(maior):
            print("Voce errou! O seu chute foi maior que o numero secreto.")
        elif (menor):
            print("Voce errou! O seu chute foi menor que o numero secreto.")
        pontos_perdidos = abs(numero_secreto - chute) #pontos perdidos da rodada
        pontos =  pontos - pontos_perdidos #subtraindo os pontos perdidos da pontuacao total 



