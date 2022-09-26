def leitorPagina(url):
    import urllib.request
    pagina = urllib.request.urlopen(url)
    pagina = pagina.read().decode("utf8")
    return pagina

def leitorPreco(pagina):
    inicio = pagina.find('>$') + 2
    fim = pagina.find('</', inicio)
    preco = pagina[inicio:fim]
    return preco

def main():

    url = str(input(f"\nInsira o url da página: "))
    pagina = leitorPagina(url)
    preco = float(leitorPreco(pagina))

    while preco > 4.7:
        print(f"\nTa caro! ${preco} ")
    print(f"\nAgora da! ${preco} ")


if __name__ == "__main__":
    main()
    

