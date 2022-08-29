from random import shuffle, randint

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

