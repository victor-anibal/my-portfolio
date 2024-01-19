import random
print(8*"*//*")
print("Bem-vindo ao jogo de adivinhação!")
print(8*"*//*")

numeroMax = 100
numero_secreto = (random.randrange(1, numeroMax + 1))
print(numero_secreto)
total_tentativa = 3
rodada = 1
chute = -1
tentativa = total_tentativa
print("Neste jogo você tem até 3 tentativas para acertar o número secreto!!!")


for rodada in range(1, total_tentativa + 1):

    print(f"Tentativa {rodada} de 3")
    chute = int(input(f"Digite um número entre 1 e {numeroMax}: "))
    tentativa = tentativa - 1
    if chute < 1 or chute > 100:
        print(f'Você deve digitar um número entre 1 e {numeroMax}!')
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
    if tentativa == 0 and chute != numero_secreto:
        print(" Seu número de tentativas acabou!\n Mas ainda não é o fim.\n Tente novamente e ganhe na próxima vez!")

print("@@@-Fim de jogo-@@@")
