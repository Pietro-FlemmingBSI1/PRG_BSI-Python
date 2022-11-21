from listasPalavras import escolha
from modificador import selecionador, ordenador, fraseErro


def main(): # Roda o programa principal.
    tema = int(input("Escolha o tema:\n1 - Cores\n2 - Objetos\n3 - Países\n")) # Usuário escolhe o tema.
    dificuldade = int(input("Escolha a dificuldade:\n1 - Fácil\n2 - Médio\n3 - Difícil\n")) # Usuário escolhe a dificuldade.
    lista_palavras = escolha(tema, dificuldade) # Gera uma lista com as palavras que se encaixam nas escolhas do usuário.
    palavra = selecionador(lista_palavras) # Seleciona quais será a palavra para adivinhar e qual frase será apresentada ao usuário caso ele perca.
    palavra_embaralhada = ordenador(palavra) # Pega a palavra selecionada e embaralha, retornando a palavra pronta para o usuário.
    
    print(f"\nA palavra escolhida foi:{palavra_embaralhada}")
    verificador(palavra)

    continuar = int(input("Deseja continuar ? 1- Sim 2- Não \n")) # Questiona se o usuário quer jogar novamente.
    if continuar == 1: main()

def verificador(palavra): # Verifica se o chute foi correto ou não.
    tentativas = 0 # Contador de tentativas do usuário.
    limiteTetativas = 5 # Limite de tentativas do usuário.
    while tentativas < limiteTetativas:
        chute = str(input(f"\nVocê tem {limiteTetativas - tentativas} restantes\nQual a palavra?\n")) # Usuário tenta acertar a palavra original.
        if chute == palavra:
            print("Parabéns! Você acertou.\n")
            print(f"Voce precisou de: {tentativas+1} tentativas\n")
            break
        else:
            tentativas += 1
            print(fraseErro())
    print(f"\nA palavra era: {palavra}\n")
    



if __name__ == "__main__":
    main()
