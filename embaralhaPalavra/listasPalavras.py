def escolha(tema, dificuldade):
    # Listas com opções de temas.
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
        "portugal",
        "espanha",
        "italia",
        "franca",
        "cazaquistao",
        "groenlandia",
        "madagascar"
    ]
    lista_palavras = [] # Lista onde será adicionada as palavra que passarem no filtro das escolhas do usuário.

    if tema == 1:
        for p in lista_cores:
            if len(p) <= 5 and dificuldade == 1:
                lista_palavras.append(p)
            elif len(p) > 5 and len(p) <= 7 and dificuldade == 2:
                lista_palavras.append(p)
            elif len(p) >= 8 and dificuldade == 3:
                lista_palavras.append(p)
    elif tema == 2:
        for p in lista_objetos:
            if len(p) <= 5 and dificuldade == 1:
                lista_palavras.append(p)
            elif len(p) > 5 and len(p) <= 7 and dificuldade == 2:
                lista_palavras.append(p)
            elif len(p) >= 8 and dificuldade == 3:
                lista_palavras.append(p)
    elif tema == 3:
        for p in lista_paises:
            if len(p) <= 5 and dificuldade == 1:
                lista_palavras.append(p)
            elif len(p) > 5 and len(p) <= 7 and dificuldade == 2:
                lista_palavras.append(p)
            elif len(p) >= 8 and dificuldade == 3:
                lista_palavras.append(p)

    return lista_palavras
