def main():
    import pandas
    import matplotlib.pyplot as plt

    fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"
    dados = pandas.read_csv(fonte)
    exercicio1 = dados[["NU_IDADE","TP_SEXO"]].head(10)
    exercicio2 = dados["NU_IDADE"].unique()
    exercicio3 = len(dados["NO_MUNICIPIO_RESIDENCIA"].unique())
    exercicio4 = dados["NU_IDADE"].value_counts()
    exercicio5 = dados["SG_UF_RESIDENCIA"].hits(bins = 20,figsize = (10,8))
    #exercicio6 = dados["NU_IDADE"].value_counts().plot.pie(figsize = (10,8))
    plt.show()
    plt.close()
    



if __name__ == "__main__":
    main()