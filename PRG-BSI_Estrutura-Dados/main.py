import networkx as nx
import matplotlib.pyplot as plt

class Grafo_Direcionado:
    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas
        self.grafo = [[] for i in range(self.vertices)]
        self.contador = 0
        self.grafo_imagem = nx.DiGraph()
        self.nome_arestas = []
        self.lista_arestas = []
        self.adiciona_vertices()
        self.adiciona_arestas()

    def adiciona_vertices(self):
        for i in range(self.vertices):
            self.grafo_imagem.add_node(i+1)

    def adiciona_arestas(self):
        alpha_dict = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e', 6 : 'f', 7 : 'g', 8 : 'h', 9 : 'i', 10 : 'j', 11 : 'k', 12 : 'l', 13 : 'm', 14 : 'n', 15 : 'o', 16 : 'p', 17 : 'q', 18 : 'r', 19 : 's', 20 : 't', 21 : 'u', 22 : 'v', 23 : 'w', 24 : 'x', 25 : 'y', 26 : 'z'}
        for _ in range(self.arestas):
            u = int(input(f'Qual o vértice de partida da aresta {self.contador + 1}º?\n'))
            v = int(input(f'Qual o vértice de chegada da aresta {self.contador + 1}º?\n'))

            if u < 1 or u > self.vertices or v < 1 or v > self.vertices:
                print("Vértices inválidos.")
            else:
                self.contador += 1
                self.grafo_imagem.add_edge(u, v,)
                self.lista_arestas.append([u,v])
                self.nome_arestas.append(alpha_dict[self.contador])
                self.grafo[u - 1].append([v, alpha_dict[self.contador]])
                print("Aresta adicionada com sucesso.")

    def verifica_lista(self, lista_vertices, busca):
        for i in lista_vertices:
            if i == busca:
                return True
        return False

    def verifica_arestas(self, busca):
        lista_vertices = []
        while(self.lista_arestas != None):
            verificador = None
            j = 0
            for cont, i in enumerate(self.lista_arestas):
                if verificador == None:
                    lista_vertices.append(i[0])
                    verificador = i[0]
                lista_vertices.append(i[1])
                if self.verifica_lista(lista_vertices, busca) == True:
                    return self.lista_arestas[cont], cont+1
                self.lista_arestas[j] = []
                j += 1    

    def cria_matriz_adjacente(self):
        matriz_adjacente = [[0] * self.vertices for _ in range(self.vertices)]
        for i in range(self.vertices):
            for j in self.grafo[i]:
                matriz_adjacente[i][j[0] - 1] = 1
        return matriz_adjacente

    def cria_lista_adjacente(self):
        lista_adjacente = [[] for _ in range(self.vertices)]
        for i in range(self.vertices):
            for j in self.grafo[i]:
                lista_adjacente[i].append((i + 1, j[0], j[1]))
        return lista_adjacente

    def cria_matriz_incidencia(self):
        matriz_incidencia = [[' 0'] * self.arestas for _ in range(self.vertices)]
        alpha_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        for v in range(self.vertices):
            for i in self.grafo[v]:
                    matriz_incidencia[v][alpha_dict[i[1]]- 1] = '+1'
                    matriz_incidencia[i[0]-1][alpha_dict[i[1]]- 1] = '-1'
        return matriz_incidencia

    def imprime_matriz_adjacente(self, matriz_adjacente):
        print("Matriz de Adjacência:")
        for row in matriz_adjacente:
            print(row)

    def imprime_lista_adjacente(self, lista_adjacente):
        print("Lista de Adjacência:")
        for i, adj_list in enumerate(lista_adjacente):
            print(f"Vértice {i + 1}: ", end=" ")
            for aresta in adj_list:
                print(f"[ Aresta: {aresta[0]} -> {aresta[1]}, com Peso: {aresta[2]} ]", end=" ")
            print()

    def imprime_matriz_incidencia(self, matriz_incidencia):
        print("Matriz de Incidência:")
        for row in matriz_incidencia:
            print(row)

    def busca_profundidade(self, vertice_inicial, vertice_alvo):
        visitados = [False] * self.vertices
        return self._dfs(vertice_inicial - 1, vertice_alvo - 1, visitados)

    def _dfs(self, vertice, vertice_alvo, visitados):
        visitados[vertice] = True
        print(f'Visitando vértice {vertice + 1}')

        if vertice == vertice_alvo:
            print(f'Vértice {vertice_alvo + 1} encontrado!')
            return True

        for vizinho, _ in self.grafo[vertice]:
            if not visitados[vizinho - 1]:
                if self._dfs(vizinho - 1, vertice_alvo, visitados):
                    print(f'Vértice {vertice_alvo + 1} encontrado!')
                    return True

        return False

    def imprime_grafo(self):
        nome_arestas = dict([((n1, n2), self.nome_arestas[c]) for c, (n1, n2) in enumerate(self.grafo_imagem.edges)])
        pos = nx.spring_layout(self.grafo_imagem)
        nx.draw(self.grafo_imagem, pos, with_labels=True, font_weight='bold',)
        nx.draw_networkx_edge_labels(self.grafo_imagem, pos, edge_labels=nome_arestas, font_size=15, font_color='red')
        plt.show()

class Grafo_nao_direcionado:
    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas
        self.grafo = [[] for i in range(self.vertices)]
        self.contador = 0
        self.grafo_imagem = nx.Graph()
        self.nome_arestas = []
        self.lista_arestas = []
        self.adiciona_vertices()
        self.adiciona_arestas()

    def adiciona_vertices(self):
        for i in range(self.vertices):
            self.grafo_imagem.add_node(i+1)

    def adiciona_arestas(self):
        alpha_dict = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e', 6 : 'f', 7 : 'g', 8 : 'h', 9 : 'i', 10 : 'j', 11 : 'k', 12 : 'l', 13 : 'm', 14 : 'n', 15 : 'o', 16 : 'p', 17 : 'q', 18 : 'r', 19 : 's', 20 : 't', 21 : 'u', 22 : 'v', 23 : 'w', 24 : 'x', 25 : 'y', 26 : 'z'}
        for _ in range(self.arestas):
            u = int(input(f'Qual o vértice de partida da aresta {self.contador + 1}º?\n'))
            v = int(input(f'Qual o vértice de chegada da aresta {self.contador + 1}º?\n'))

            if u < 1 or u > self.vertices or v < 1 or v > self.vertices:
                print("Vértices inválidos.")
            else:
                self.contador += 1
                self.grafo_imagem.add_edge(u, v,)
                self.lista_arestas.append([u,v])
                self.nome_arestas.append(alpha_dict[self.contador])
                self.grafo[u - 1].append([v, alpha_dict[self.contador]])
                print("Aresta adicionada com sucesso.")

    def verifica_lista(self, lista_vertices, busca):
        for i in lista_vertices:
            if i == busca:
                return True
        return False

    def verifica_arestas(self, busca):
        lista_vertices = []
        while(self.lista_arestas != None):
            verificador = None
            j = 0
            for cont, i in enumerate(self.lista_arestas):
                if verificador == None:
                    lista_vertices.append(i[0])
                    verificador = i[0]
                lista_vertices.append(i[1])
                if self.verifica_lista(lista_vertices, busca) == True:
                    return self.lista_arestas[cont], cont+1
                self.lista_arestas[j] = []
                j += 1

    def cria_matriz_adjacente(self):
        matriz_adjacente = [[0] * self.vertices for _ in range(self.vertices)]
        for i in range(self.vertices):
            for j in self.grafo[i]:
                matriz_adjacente[i][j[0] - 1] = 1
                matriz_adjacente[j[0] - 1][i] = 1
        return matriz_adjacente

    def cria_lista_adjacente(self):
        lista_adjacente = [[] for _ in range(self.vertices)]
        for i in range(self.vertices):
            for j in self.grafo[i]:
                lista_adjacente[i].append((i + 1, j[0], j[1]))
                lista_adjacente[j[0] - 1].append((j[0], i + 1, j[1]))
        return lista_adjacente

    def cria_matriz_incidencia(self):
        matriz_incidencia = [[0] * self.arestas for _ in range(self.vertices)]
        alpha_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        for v in range(self.vertices):
            for i in self.grafo[v]:
                    matriz_incidencia[v][alpha_dict[i[1]]- 1] = 1
                    matriz_incidencia[i[0]-1][alpha_dict[i[1]]- 1] = 1
        return matriz_incidencia

    def imprime_matriz_adjacente(self, matriz_adjacente):
        print("Matriz de Adjacência:")
        for row in matriz_adjacente:
            print(row)

    def imprime_lista_adjacente(self, lista_adjacente):
        print("Lista de Adjacência:")
        for i, adj_list in enumerate(lista_adjacente):
            for aresta in adj_list:
                print(f"[ Aresta: {aresta[0]} <-> {aresta[1]}, Indicador da aresta: {aresta[2]} ] \n", end=" ")

    def imprime_matriz_incidencia(self, matriz_incidencia):
        print("Matriz de Incidência:")
        for row in matriz_incidencia:
            print(row)

    def busca_profundidade(self, vertice_inicial, vertice_alvo):
        visitados = [False] * self.vertices
        return self._dfs(vertice_inicial - 1, vertice_alvo - 1, visitados)

    def _dfs(self, vertice, vertice_alvo, visitados):
        visitados[vertice] = True
        print(f'Visitando vértice {vertice + 1}')

        if vertice == vertice_alvo:
            print(f'Vértice {vertice_alvo + 1} encontrado!')
            return True

        for vizinho, _ in self.grafo[vertice]:
            if not visitados[vizinho - 1]:
                if self._dfs(vizinho - 1, vertice_alvo, visitados):
                    print(f'Vértice {vertice_alvo + 1} encontrado!')
                    return True

        return False

    def imprime_grafo(self):
        nome_arestas = dict([((n1, n2), self.nome_arestas[c]) for c, (n1, n2) in enumerate(self.grafo_imagem.edges)])
        pos = nx.spring_layout(self.grafo_imagem)
        nx.draw(self.grafo_imagem, pos, with_labels=True, font_weight='bold',)
        nx.draw_networkx_edge_labels(self.grafo_imagem, pos, edge_labels=nome_arestas, font_size=15, font_color='red')
        plt.show()

graph_type = input("Qual tipo de grafo você quer criar? (Direcionado / Não direcionado): ").lower()

if graph_type == "direcionado":
    v = int(input('Digite a quantidade de vértices: \n'))
    a = int(input('Quantas arestas possui o grafo? \n'))
    g = Grafo_Direcionado(v, a)

elif graph_type == "não direcionado" or graph_type == "nao direcionado":
    v = int(input('Digite a quantidade de vértices: \n'))
    a = int(input('Quantas arestas possui o grafo? \n'))
    g = Grafo_nao_direcionado(v, a)

else:
    print("Escolha inválida.")

matriz_adjacente = g.cria_matriz_adjacente()
lista_adjacente = g.cria_lista_adjacente()
matriz_incidencia = g.cria_matriz_incidencia()

vertice_inicial = int(input('Digite o vértice inicial para a busca em profundidade: '))
vertice_alvo = int(input('Digite o vértice alvo para a busca em profundidade: '))
g.busca_profundidade(vertice_inicial, vertice_alvo)

g.imprime_matriz_adjacente(matriz_adjacente)
g.imprime_lista_adjacente(lista_adjacente)
g.imprime_matriz_incidencia(matriz_incidencia)
g.imprime_grafo()
print(g.verifica_arestas(4))