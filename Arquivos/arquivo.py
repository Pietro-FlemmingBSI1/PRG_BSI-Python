from matplotlib

if __name__ == "__main__":
    with open("Alice_Maravilhas.txt") as file:
        texto = file.read().lower()
    
    limpa_texto = [l for l in texto if l.isalpha()]

    lista_letras = {}

    for l in limpa_texto:
        lista_letras = l.get(l, 0) + 1
    


