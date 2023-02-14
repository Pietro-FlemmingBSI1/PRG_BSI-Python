def leitor_texto():
    with open("Alice_Maravilhas.txt") as file:
        texto = file.read().lower()
    return texto

def quantidade_letras(texto):
    lista_letras = {}

    for l in texto:
        lista_letras[l] = lista_letras.get(l, 0) + 1
    from collections import Counter
    lista_letras = Counter(lista_letras)

    return lista_letras


if __name__ == "__main__":    

    import matplotlib.pyplot as plt

    texto = [l for l in leitor_texto() if l.isalpha()]

    rotulos, valores = zip(*quantidade_letras(texto).most_common(50))
    plt.title("Frequencia de letras")
    plt.bar(rotulos,valores)
    plt.show()
    plt.savefig("Livro.png")
    plt.close() 


