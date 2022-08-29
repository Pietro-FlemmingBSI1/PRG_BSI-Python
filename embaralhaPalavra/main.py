from listasPalavras import escolha
from modificador import selecionador,ordenador

def main():
    tema = int(input("Escolha o tema:\n1 - Cores\n2 - Objetos\n3 - Países\n"))
    dificuldade = int(
        input("Escolha a dificuldade:\n1 - Fácil\n2 - Médio\n3 - Difícil\n")
    )
    lista_palavras = escolha(tema, dificuldade)

    palavra, multivacional = selecionador(lista_palavras)
    palavra_embaralhada = ordenador(palavra)
    print(f"\nA palavra escolhida foi:{palavra_embaralhada}")

    tentativas = 0
    while tentativas < 5:
        chute = str(input("Qual a palavra?\n"))
        if chute == palavra:
            print("Parabéns! Você acertou.\n")
            break
        else:
            tentativas += 1
    print(f"\nA palavra era:{palavra}\n")
    if tentativas == 5:
        print(multivacional)
    else:
        print(f"Voce precisou de: {tentativas+1} tentativas\n")


if __name__ == "__main__":
    main()
