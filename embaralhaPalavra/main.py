from random import shuffle, randint


def escolha(tema, dificuldade):
    lista_cores = [
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
        "azul",
        "bege",
        "rosa",
        "esmeralda",
        "carmesim",
        "jade",
        "magenta",
        "turquesa",
        "violeta",
        "framboesa",
    ]
    lista_objetos = [
        "camiseta",
        "livro",
        "faca",
        "computador",
        "cola",
        "fita",
        "celular",
        "notebook",
        "caneta",
        "grampo",
        "garfo",
        "palito",
        "bala",
        "vaso",
        "frigideira",
        "panela",
        "monitor",
    ]
    lista_paises = [
        "brasil",
        "china",
        "austria",
        "macedonia",
        "inglaterra",
        "islandia",
        "japao",
        "australia",
        "cuba",
        "canada",
        "argentina",
        "colombia",
        "venezuela",
        "alemanha",
        "postugal",
        "espanha",
        "italia",
        "franca",
    ]
    lista = []
    lista_palavras = []

    if tema == 1:
        lista = lista_cores
    elif tema == 2:
        lista = lista_objetos
    elif tema == 3:
        lista = lista_paises

    for p in lista:
        if len(p) <= 5 and dificuldade == 1:
            lista_palavras.append(p)
        elif len(p) > 5 and len(p) <= 7 and dificuldade == 2:
            lista_palavras.append(p)
        elif len(p) >= 8 and dificuldade == 3:
            lista_palavras.append(p)
    return lista_palavras


def selecionador(lista_palavras):
    lista_falhou = [
        "Não foi dessa vez, tente denovo, eu sei que você consegue!",
        "Essa era díficil mesmo, mas continue tentando.",
        "Essa foi por pouco, que tal tentar denovo.",
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
    tema = int(input("Escolha o tema:\n1 - Cores\n2 - Objetos\n3 - Países\n"))
    dificuldade = int(
        input("Escolha a dificuldade:\n1 - Fácil\n2 - Médio\n3 - Difícil\n")
    )
    lista_palavras = escolha(tema, dificuldade)

    palavra, multivacional = selecionador(lista_palavras)
    palavra_embaralhada = ordenador(palavra)
    print(f"\nA palavra escolhida foi:{palavra_embaralhada}")

    tentativas = 0
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
