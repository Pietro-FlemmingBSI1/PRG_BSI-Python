def leitorPagina(url):
    import urllib.request
    pagina = urllib.request.urlopen(url)
    pagina = pagina.read().decode("utf8")
    inicio = pagina.find('>$') + 2
    fim = pagina.find('</', inicio)
    preco = float(pagina[inicio:fim])
    return preco


def verificador(url):
    import time
    preco = 5
    while preco >=4.99:
        time.sleep(5)
        preco = leitorPagina(url)
        print(f"\nPreço acima do requisitado! ${preco}")
    return preco


def main():
    from configEmail import sendEmail

    url = str(input(f"\nInsira o url da página: "))
    email = str(input(f"\nInsira o email que ira receber o aviso: "))
    preco = verificador(url)
    sendEmail(email,preco)

if __name__ == "__main__":
    main()
    

