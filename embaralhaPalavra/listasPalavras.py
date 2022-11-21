def escolha(tema, dificuldade): # Recebe um tema e uma dificuldade e retorna uma lista de palavras que se encaixam nos parâmetros. 
    if tema == 1: lista_palavras = temaCores()
    elif tema == 2: lista_palavras = temaObjetos()
    elif tema == 3: lista_palavras = temaPaises()
    lista_palavras = definindoDificuldade(lista_palavras,dificuldade)

    return lista_palavras

def temaCores(): # Lisca com as palavras do tema cores.
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
    return lista_cores

def temaObjetos():# Lisca com as palavras do tema objetos.
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
    return lista_objetos

def temaPaises(): # Lisca com as palavras do tema Países.
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
    return lista_paises

def definindoDificuldade(lista_completa, dificuldade): # Gera uma lista apartir da dificuldade.
    lista = []
    for p in lista_completa:
        if len(p) <= 5 and dificuldade == 1:
            lista.append(p)
        elif len(p) > 5 and len(p) <= 7 and dificuldade == 2:
            lista.append(p)
        elif len(p) >= 8 and dificuldade == 3:
            lista.append(p)
    return lista