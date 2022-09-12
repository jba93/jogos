import random
import jogos


def jogar():
    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print("Níveis: 1 (Fácil) | 2 (Médio) | 3 (Difícil)")

    nivel = "4"
    while nivel != "1" and nivel != "2" and nivel != "3":
        nivel = input("Escolha seu nível: ")
        if nivel == "1":
            total_tentativas = 10
            print("Nível fácil")
        elif nivel == "2":
            total_tentativas = 5
            print("Nível médio")
        elif nivel == "3":
            total_tentativas = 3
            print("Nível difícil")
        else:
            print("Opção inválida.")

    for tentativa in range(1, total_tentativas+1):
        print("Tentativa {} de {}".format(tentativa, total_tentativas))

        chute = "a"
        while not chute.isdigit():
            chute = input("Digite um número inteiro entre 1 e 100: ")
            if chute.isdigit():
                chute = int(chute)
                break
            else:
                print("Valor inválido.")

        acertou = (numero_secreto == chute)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)

        if(chute<=0 or chute>100):
            print("O número deve ser inteiro de 1 a 100.")
            continue

        if (acertou):
            print("Parabéns, você acertou!")
            break
        elif(maior):
            print("Tente um número menor.")
        elif(menor):
            print("Tente um número maior.")
        pontos = pontos - abs(numero_secreto - chute)

    print("Fim de jogo | Número secreto: {} | {} pontos".format(numero_secreto, pontos))
    novo_jogo()


def novo_jogo():
    opcao = "Y"
    while opcao != "S" and opcao != "N":
        opcao = input("Deseja jogar novamente? S/N ").upper().strip()

        if opcao == "S":
            jogar()
        elif opcao == "N":
            jogos.escolhe_jogo()
        else:
            print("Opção inválida.")


def imprime_mensagem_abertura():
    print("*" * 35)
    print("Bem vindo(a) ao jogo de Adivinhação!")
    print("*" * 35)
    jogar()


if (__name__ == "__main__"):
    imprime_mensagem_abertura()
