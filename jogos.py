import forca
import adivinhacao
import sys

def escolhe_jogo():
    print("*" * 35)
    print("Escolha seu jogo!")
    print("*" * 35)

    jogo = 3
    while jogo != 1 and jogo != 2 and jogo != 0:
        jogo = input("1 (Forca) | 2 (Adivinhação) | 0 (Sair) | Opção: ").strip()

        if jogo == "1":
            forca.imprime_mensagem_abertura()
        elif jogo == "2":
            adivinhacao.imprime_mensagem_abertura()
        elif jogo == "0":
            print("Tchau, tchau!")
            sys.exit()
        else:
            print("Opção inválida.")


if (__name__ == "__main__"):
    escolhe_jogo()
