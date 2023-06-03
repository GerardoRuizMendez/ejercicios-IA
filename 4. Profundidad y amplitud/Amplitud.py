import numpy as np

# PARA ELEGIR QUE PROBLEMA EJECUTAR IR A LAS VARIABLES DEL FINAL DEL ARCHIVO 
class Nodo:
    def __init__(self,tablero, visitados=[]):
        self.tablero=tablero
        self.hijos=[]
        self.visitados=visitados
        self.visitados.append(tablero)
    def calculaHijos(self):
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                if(self.tablero[i][j]==""):
                    if(i>0):
                        #hijo arriba
                        aux=np.zeros((len(self.tablero),len(self.tablero[i])),dtype=str)
                        aux[:][:]=self.tablero[:][:]
                        aux[i][j]=self.tablero[i-1][j]
                        aux[i-1][j]=self.tablero[i][j]
                        
                        aux2=[]
                        for k in range(len(self.visitados)):
                            n=np.zeros((len(self.visitados[0]),len(self.visitados[0][0])),dtype=str)
                            n[:][:]=self.visitados[k][:][:]
                            aux2.append(n)
                        self.hijos.append(Nodo(aux,aux2))
                    if(j<len(self.tablero)-1):
                        #hijo derecha
                        aux=np.zeros((len(self.tablero),len(self.tablero[i])),dtype=str)
                        aux[:][:]=self.tablero[:][:]
                        aux[i][j]=self.tablero[i][j+1]
                        aux[i][j+1]=self.tablero[i][j]

                        aux2=[]
                        for k in range(len(self.visitados)):
                            n=np.zeros((len(self.visitados[0]),len(self.visitados[0][0])),dtype=str)
                            n[:][:]=self.visitados[k][:][:]
                            aux2.append(n)
                        self.hijos.append(Nodo(aux,aux2))
                    if(i<len(self.tablero)-1):
                        #hijo abajo
                        aux=np.zeros((len(self.tablero),len(self.tablero[i])),dtype=str)
                        aux[:][:]=self.tablero[:][:]
                        aux[i][j]=self.tablero[i+1][j]
                        aux[i+1][j]=self.tablero[i][j]

                        aux2=[]
                        for k in range(len(self.visitados)):
                            n=np.zeros((len(self.visitados[0]),len(self.visitados[0][0])),dtype=str)
                            n[:][:]=self.visitados[k][:][:]
                            aux2.append(n)
                        self.hijos.append(Nodo(aux,aux2))
                    if(j>0):
                        #hijo izquierda
                        aux=np.zeros((len(self.tablero),len(self.tablero[i])),dtype=str)
                        aux[:][:]=self.tablero[:][:]
                        aux[i][j]=self.tablero[i][j-1]
                        aux[i][j-1]=self.tablero[i][j]

                        aux2=[]
                        for k in range(len(self.visitados)):
                            n=np.zeros((len(self.visitados[0]),len(self.visitados[0][0])),dtype=str)
                            n[:][:]=self.visitados[k][:][:]
                            aux2.append(n)
                        self.hijos.append(Nodo(aux,aux2))
    @staticmethod    
    def comprobar(nodo, objetivo):
        for i in range(len(nodo.tablero)):
            for j in range(len(nodo.tablero[i])):
                if(not nodo.tablero[i][j]==objetivo.tablero[i][j]):
                    return False
        return True

class NodoGranjero:
    def __init__(self,lado1,lado2,granjero, visitados=[]):
        self.granjero=granjero
        self.lado1=lado1
        self.lado2=lado2
        self.hijos=[]
        self.visitados=visitados
        self.visitados.append(str(self.lado1)+" 🌊🌊🌊 " +str(self.lado2) +" Granjero en: "+self.granjero)

    def calculaHijos(self):
        if(self.granjero=="izquierda"):
            for n in self.lado1:
                auxLado1=[]
                auxLado1[:]=self.lado1[:]
                auxLado2=[]
                auxLado2[:]=self.lado2[:]

                auxLado2.append(n)
                auxLado1.remove(n)
                if(not self.comer(auxLado1)):
                    aux2=[]
                    for k in range(len(self.visitados)):
                        n=[]
                        n=self.visitados[k]
                        aux2.append(n)
                    #self.hijos.append(Nodo(aux,aux2))
                    self.hijos.append(NodoGranjero(auxLado1,auxLado2,"derecha",aux2))
            if(not self.comer(self.lado1)):
                auxLado1=[]
                auxLado1[:]=self.lado1[:]
                auxLado2=[]
                auxLado2[:]=self.lado2[:]

                aux2=[]
                for k in range(len(self.visitados)):
                    n=[]
                    n=self.visitados[k]
                    aux2.append(n)
                self.hijos.append(NodoGranjero(auxLado1,auxLado2,"derecha",aux2)) 
        
        if(self.granjero=="derecha"):
            for n in self.lado2:
                auxLado1=[]
                auxLado1[:]=self.lado1[:]
                auxLado2=[]
                auxLado2[:]=self.lado2[:]

                auxLado1.append(n)
                auxLado2.remove(n)
                if(not self.comer(auxLado2)):
                    aux2=[]
                    for k in range(len(self.visitados)):
                        n=[]
                        n=self.visitados[k]
                        aux2.append(n)
                    self.hijos.append(NodoGranjero(auxLado1,auxLado2,"izquierda",aux2))
            if(not self.comer(self.lado2)):
                auxLado1=[]
                auxLado1[:]=self.lado1[:]
                auxLado2=[]
                auxLado2[:]=self.lado2[:]

                aux2=[]
                for k in range(len(self.visitados)):
                    n=[]
                    n=self.visitados[k]
                    aux2.append(n)
                self.hijos.append(NodoGranjero(auxLado1,auxLado2,"izquierda",aux2))
    @staticmethod    
    def comprobar(nodo, objetivo):
        for n in nodo.lado1:
            if not n in objetivo.lado1: return False
        for n in nodo.lado2:
            if not n in objetivo.lado2: return False
        if not nodo.granjero==objetivo.granjero: return False
        return True
    @staticmethod
    def comer(array): #comprobamos que nada se coma a nada xd
        if array.__contains__("🐺") and array.__contains__("🐐"):
            return True
        if array.__contains__("🐐") and array.__contains__("🥬"):
            return True
        return False
    def imprimir(self):
        print(str(self.lado1) +str(self.lado2) +self.granjero)

def amplitud(nodo, objetivo):
    global encontrado
    cola=[]
    cola.append(nodo)
    while(not encontrado):

        actual=cola.pop(0)
        if(actual.comprobar(actual, objetivo)):
            encontrado=actual
            return
        actual.calculaHijos()
        for n in actual.hijos:
            cola.append(n)

nodoOrigen=Nodo([['1','2','3'],['4','5','6'],['7','8','']],[])
nodoObjetivo=Nodo([['1','2','3'],['7','','4'],['8','6','5']],[])
# COMENTAR LAS SIGUIENTES DOS VARIABLES PARA EJECUTAR EL CODIGO DEL PUZZLE DESLIZANTE
nodoOrigen=NodoGranjero(["🐺","🥬","🐐"],[],"izquierda",[])
nodoObjetivo=NodoGranjero([],["🐺","🥬","🐐"],"derecha",[])

encontrado=False

amplitud(nodoOrigen, nodoObjetivo)
for n in encontrado.visitados:
    print(n)
    print("---")