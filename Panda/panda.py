def main():
    import pandas

    fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"
    dados = pandas.read_csv(fonte)
    exercicio1 = tarefa1(dados)
    exercicio2 = tarefa2(dados)
    exercicio3 = tarefa3(dados)
    exercicio4 = tarefa4(dados)
    exercicio5 = tarefa5(dados)
    exercicio6 = tarefa6(dados)
    
    print(exercicio1)
    print(exercicio2)
    print(exercicio3)
    print(exercicio4)
    print(exercicio5)
    print(exercicio6)

    
def tarefa1(dados):
    return dados[["NU_IDADE","TP_SEXO"]].head(10)

def tarefa2(dados):
    return dados["NU_IDADE"].unique()

def tarefa3(dados):
    return len(dados["NO_MUNICIPIO_RESIDENCIA"].unique())

def tarefa4(dados):
    return dados["NU_IDADE"].value_counts()

def tarefa5(dados):
    import matplotlib.pyplot as plt
    return dados["SG_UF_RESIDENCIA"].hits(bins = 20,figsize = (10,8))
    plt.show()
    plt.close()

def tarefa6(dados):
    import matplotlib.pyplot as plt
    return dados["NU_IDADE"].value_counts().plot.pie(figsize = (10,8))
    plt.show()
    plt.close()


if __name__ == "__main__":
    main()