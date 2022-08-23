from random import shuffle, randint


def selecionador():
    lista_falhou = [
        "Não foi dessa vez, tente denovo, eu sei que você consegue!",
        "Essa era díficil mesmo, mas continue tentando.",
        "Essa foi por pouco, que tal tentar denovo.",
    ]
    lista_palavras = [
        "roxo",
        "preto",
        "branco",
        "cinza",
        "amarelo",
        "verde",
        "vermelho",
        "ciano",
        "marrom",
        "laranja",
    ]
    palavra = randint(0, len(lista_palavras) - 1)
    palavra = lista_palavras[palavra]
    multivacional = randint(0, len(lista_falhou) - 1)
    multivacional = lista_falhou[multivacional]
    return palavra, multivacional


def ordenador(palavra):
    palavra_lista = []
    palavra = palavra.lower()
    for l in palavra:
        palavra_lista.append(l)
    shuffle(palavra_lista)
    palavra_embaralhada = ""
    for l in palavra_lista:
        palavra_embaralhada += l
    return palavra_embaralhada


def main():
    tentativas = 0
    palavra, multivacional = selecionador()
    palavra_embaralhada = ordenador(palavra)
    print(f"\nA palavra escolhida foi:{palavra_embaralhada}")
    while tentativas < 5:
        chute = str(input("Qual a palavra?\n"))
        if chute == palavra:
            print("Parabéns! Você acertou.\n")
            break
        else:
            tentativas += 1
    print(f"\nA palavra era:{palavra}\n")
    if tentativas == 5:
        print(multivacional)
    else:
        print(f"Voce precisou de:{tentativas+1} tentativas\n")


if __name__ == "__main__":
    main()
