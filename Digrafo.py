

class GrafoDrigido():
    matriz : list
    
    def __init__(self, nodos) -> None:
        self.matriz = [[0 for _ in range(nodos)] for _ in range(nodos)]

    def arista(self, i, j):
        self.matriz [i][j] = 1
        
    def GradoEntrada(self,nodo): ### MUESTRA SI ES SUMIDERO Y SI TIENE ENTRADAS MUESTRA CUANTAS
        i = 0
        numEntradas = 0
        while i < len(self.matriz):
            if self.matriz[i-1][nodo] == 1:
                numEntradas +=1
            i+=1
        return(int(numEntradas))
            
    def GradoSalida(self,nodo):
        i = 0
        numEntradas = 0
        while i < len(self.matriz):
            if self.matriz[nodo][i-1] == 1:
                numEntradas +=1
            i+=1
        return numEntradas
     
    def fuente(self, nodo):
        if self.GradoEntrada(nodo) == 0:
            if self.GradoSalida(nodo) > 0:
                x = True
            else:
                x = False
        else:
            x = False
        return x
        
    def sumidero(self, nodo):
        if self.GradoSalida(nodo) == 0:
            if self.GradoEntrada(nodo) > 0:
                x = True
            else:
                x = False
        else:
            x = False
        return x
        
    
    def Camino(self):
           pass
            
            

    def mostrar(self):
        for i in self.matriz:
            print(i)

if __name__ == "__main__":
    G=GrafoDrigido(7)
    G.arista(1,2)
    G.arista(2,3)
    G.arista(3,4)
    G.arista(4,2)
    G.arista(5,4)
    G.arista(5,6)
    G.mostrar()
    G.GradoEntrada(4)
    G.GradoSalida(1)
    res = G.sumidero(4)
    Res2 = G.fuente(5)
    print(f"\nEl nodo es sumidero: {res}")
    print(f"El nodo es fuente: {Res2}")
    