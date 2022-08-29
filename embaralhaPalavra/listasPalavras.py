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
