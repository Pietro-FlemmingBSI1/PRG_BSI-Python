class busca_grafo():

    def __init__(self, lista_adj, busca):
        self.lista_adj = lista_adj
        self.busca = busca
    
    def verifica_lista(self, lista_arestas):
        for i in lista_arestas:
            if i == self.busca:
                return True
        return False

    def verifica_vertice(self):
        lista_arestas = []
        while(self.lista_adj != None):
            verificador = None
            j = 0
            for i in self.lista_adj:
                if verificador == None:
                    lista_arestas.append(i[0])
                    verificador = i[0]
                if i[0] == verificador:
                    lista_arestas.append(i[1])
                    self.lista_adj[j] = []
                j += 1
                if self.verifica_lista(lista_arestas) == True:
                    return self.lista_adj.index(self.busca)
                

#Teste

vasco = busca_grafo([[1,2],[1,3],[2,4],[3,4]],3)

print(vasco.verifica_vertice())