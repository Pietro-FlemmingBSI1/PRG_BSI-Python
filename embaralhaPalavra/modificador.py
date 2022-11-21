from random import shuffle, choice

def selecionador(lista_palavras): # Recebe uma lista de palavras e retorna uma palavra e uma frase de derrota.
    palavra = choice(lista_palavras) # Escolhe a palavra que será embaralhada.
    return palavra

def fraseErro():
        # Lista de mensagens caso o usuário perca.
    lista_falhou = [
        "Não foi dessa vez, tente denovo, eu sei que você consegue!",
        "Essa era díficil mesmo, mas continue tentando.",
        "Essa foi por pouco, que tal tentar denovo.",
    ]

    multivacional = choice(lista_falhou) # Escolhe a mensagem caso o usuário perca.
    return multivacional


def ordenador(palavra): # Recebe uma palavra e retorna a mesma com a ordem das letras trocadas.
    palavra_lista = []
    palavra = palavra.lower()
    for l in palavra:
        palavra_lista.append(l) # Gera uma lista das letras da palavra selecionada.
    shuffle(palavra_lista) # Coloca as letras em ordem aleatória.
    palavra_embaralhada = ""
    for l in palavra_lista:
        palavra_embaralhada += l # Retorna a lista de letras em uma palavra.
    return palavra_embaralhada

