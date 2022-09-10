from random import shuffle, choice

def selecionador(lista_palavras):
    # Lista de mensagens caso o usuário perca.
    lista_falhou = [
        "Não foi dessa vez, tente denovo, eu sei que você consegue!",
        "Essa era díficil mesmo, mas continue tentando.",
        "Essa foi por pouco, que tal tentar denovo.",
    ]

    palavra = choice(lista_palavras) # Escolhe a palavra que será embaralhada.
    multivacional = choice(lista_falhou) # Escolhe a mensagem caso o usuário perca.
    return palavra, multivacional


def ordenador(palavra):
    palavra_lista = []
    palavra = palavra.lower()
    for l in palavra:
        palavra_lista.append(l) # Gera uma lista das letras da palavra selecionada.
    shuffle(palavra_lista) # Coloca as letras em ordem aleatória.
    palavra_embaralhada = ""
    for l in palavra_lista:
        palavra_embaralhada += l # Retorna a lista de letras em uma palavra.
    return palavra_embaralhada

