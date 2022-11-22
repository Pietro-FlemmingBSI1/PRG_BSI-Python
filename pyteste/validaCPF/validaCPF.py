"""
Validaçao do CPF

Os dois dígitos de verificação do CPF (constituído de 9 dígitos) são calculados através de um complicado algoritmo:

Etapa 1: cálculo de DV1
    Soma 1: soma dos produtos de cada dígito por um peso de 2 a 10, na ordem inversa (do nono para o primeiro).
    Multiplique a soma 1 por 10 e calcule o resto da divisão do resultado por 11. Se der 10, DV1 é zero,caso contrário o DV1 é o próprio resto.

Etapa 2: cálculo de DV2
    Soma 2: soma dos produtos de cada dígito por um peso de 3 a 11, também na ordem inversa.
    Adicione a Soma 2 ao dobro do DV1, multiplique por 10 e calcule o resto da divisão do resultado por 11.
    Se der 10, DV2 é zero, caso contrário o DV2 é o próprio resto.

Etapa 3: Multiplique DV1 por 10, some com DV2 e você tem o número de controle do CPF.

Exemplo: para o CPF 398 136 146, temos:

Etapa 1: 2x6 + 3x4 + 4x1 + 5x6 + 6x3 + 7x1 + 8x8 + 9x9 + 10x3 = 258
258 * 10 mod 11 = 6, portanto, DV1 = 6

Etapa 2: 3x6 + 4x4 + 5x1 + 6x6 + 7x3 + 8x1 + 9x8 + 10x9 + 11x3 = 299
(299 + 6x2)x10 mod 11 = 3150 mod 11 = 8, portanto DV2 = 8

Etapa 3: DV1x10 + DV2 = 6x10 + 8 = 68, que é o número procurado.
"""


def dv1_bruto(cpf):
    """Calcula o DV1 do CPF"""

    return sum(((i + 2) * int(d) for i, d in enumerate(cpf[::-1])))


def dv1(cpf):
    """Calcula o DV1 do CPF"""

    resultado = dv1_bruto(cpf) * 10 % 11 
    return resultado if resultado < 10 else 0

def dv2_bruto(cpf):
    """Calcula o DV2 do CPF"""

    return sum(((i + 3) * int(d) for i, d in enumerate(cpf[::-1])))

def dv2(cpf):
    """Calcula o DV2 do CPF"""

    resultado = (dv2_bruto(cpf) + dv1(cpf) * 2) * 10 % 11
    return resultado if resultado < 10 else 0

def dv(cpf):
    """Calcula o DV final do CPF"""

    return str(dv1(cpf)) + str(dv2(cpf))

def arrumaCPF(cpf):
    if "." or "-" in cpf:
        cpf = cpf.replace(".","")
        cpf = cpf.replace("-","")
    if len(cpf) == 11:
        verficador = cpf[9:]
        cpf = cpf[:9]
        return cpf,verficador
    elif len(cpf) == 9:
        return cpf, None
    else:
        return None, None

def geradorCPF(quantidade):
    import random as rd
    lista_CPFs = []
    for cpf in range(0, quantidade):
        cpf = str(rd.random())[2:11]
        verificador = dv(cpf)
        cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + verificador
        lista_CPFs.append(cpf)
    if quantidade == 1:
        return lista_CPFs[0]
    else:
        return lista_CPFs



def main():
    escolha = int(input("1-Validar CPF / 2-Gerar CPF\n"))
    if escolha == 1: 
        cpf = str(input("Insira o CPF:\n"))
        cpfArrumado, verificador = arrumaCPF(cpf)
        if cpfArrumado != None and verificador != None:
            if dv(cpfArrumado) == verificador:
                print("CPF Válido")
        elif cpfArrumado != None and verificador == None:
            verificador = dv(cpfArrumado)
            print("Seu verificador de CPF é:",verificador)
        elif cpfArrumado == None:
            print("CPF Inválido")
    elif escolha == 2:
        quantidade = int(input("Quantos CPFs você deseja ?\n"))
        if quantidade == 1:
            print("O CPF gerado foi:",geradorCPF(quantidade))
        else:
            print("A lista de CPFs gerados foram:",geradorCPF(quantidade))
    voltarComeco = int(input("\nDeseja fazer outra consulta ? 1- Sim / 2- Não\n"))
    if voltarComeco == 1:
        main()


if __name__ == "__main__":
    main()
