import random
import unidecode
import jogos


def jogar():
    palavra_secreta, dica = carrega_palavra_secreta_dica()
    palavra_acertada = []

    for letra in palavra_secreta:
        if letra != "-":
            palavra_acertada.append("_")
        else:
            palavra_acertada.append("-")

    print("A dica é: {}".format(dica))
    print(palavra_acertada)

    tentativas = calcula_tentativas(palavra_secreta)

    acertou = False
    enforcou = False
    erros = 0

    while not enforcou and not acertou:
        chute = unidecode.unidecode(solicita_chute())
        palavra_secreta_unidecode = unidecode.unidecode(palavra_secreta)

        if (chute in palavra_secreta_unidecode):
            marca_chute_correto(chute, palavra_secreta_unidecode, palavra_secreta, palavra_acertada)
        else:
            print("Letra não encontrada. Restam {} tentativas.".format(tentativas - erros - 1))
            erros += 1

        enforcou = (erros == tentativas)
        acertou = "_" not in palavra_acertada
        print(palavra_acertada)

    if (acertou):
        print("Parabéns! Você venceu!")
        novo_jogo()
    else:
        print("Você perdeu! A palavra era {}.".format(palavra_secreta))
        novo_jogo()


def imprime_mensagem_abertura():
    print("*" * 35)
    print("Bem vindo(a) ao jogo de Forca!")
    print("*" * 35)
    jogar()


def carrega_palavra_secreta_dica():
    numero = str(random.randrange(1, 4))
    nome_arquivo = "palavras"+numero+".txt"
    arquivo = open(nome_arquivo, encoding="utf-8", mode="r")
    dica = arquivo.readline().strip().upper()
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return (palavra_secreta, dica)


def solicita_chute():
    chute = "1"
    while not chute.isalpha():
        chute = input("Chute uma letra: ")
        if chute.isalpha():
            return chute.upper().strip()


def marca_chute_correto(chute, palavra_secreta_unidecode, palavra_secreta, palavra_acertada):
    index = 0
    for letra in palavra_secreta_unidecode:
        if chute == letra:
            palavra_acertada[index] = palavra_secreta[index]
        index += 1

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


def calcula_tentativas(palavra_secreta):
    letras = []
    for letra in palavra_secreta:
        if letra not in letras and letra!="-":
            letras.append(letra)
    return len(letras)-1


if (__name__ == "__main__"):
    imprime_mensagem_abertura()
