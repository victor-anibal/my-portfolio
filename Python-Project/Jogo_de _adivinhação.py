import random
print(8*"*//*")
print("Bem-vindo ao jogo de adivinhação!")
print(8*"*//*")



print("(1) Fácil\n(2) Médio\n(3) Difícil")

nivel = 0

while nivel <= 0 or nivel > 3:
    nivel = int(input("Defina um nível: "))
    print("Escolha um número entre 1 e 3!")


pontos = 1000
total_tentativa = 0

if nivel == 1:
    numero_max = 100
    total_tentativa = 20

elif nivel == 2:
    numero_max = 500
    total_tentativa = 15

else:
    numero_max = 1000
    total_tentativa = 10

numero_secreto = (random.randrange(1,  numero_max + 1))


print(numero_secreto)

rodada = 1
chute = -1
tentativa = total_tentativa
print(f"Neste jogo você tem até {total_tentativa} tentativas para acertar o número secreto!!!")


for rodada in range(1, total_tentativa + 1):

    print(f"Tentativa {rodada} de {total_tentativa}")
    chute = int(input(f"Digite um número entre 1 e {numero_max}: "))
    tentativa = tentativa - 1
    if chute < 1 or chute > numero_max:
        print(f'Você deve digitar um número entre 1 e {numero_max}!')
        continue


    menor = chute < numero_secreto
    maior = chute > numero_secreto
    acerto = chute == numero_secreto

    if acerto:
        print(f"Parabéns! Você acertou!!!")
        break
    else:
        if menor:
            print(f"O número secreto é maior que {chute}")
        elif maior:
            print(f"O número secreto é menor que {chute}")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    if tentativa == 0 and chute != numero_secreto:
        print(" Seu número de tentativas acabou!\n Mas ainda não é o fim.\n Tente novamente e ganhe na próxima vez!")

print("@@@-Fim de jogo-@@@")
