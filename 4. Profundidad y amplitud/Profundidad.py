import numpy as np

limiteProfundidad=50 #limite de profundidad
# PARA ELEGIR QUE PROBLEMA EJECUTAR IR A LAS VARIABLES DEL FINAL DEL ARCHIVO 

class Nodo:
    def __init__(self,tablero):
        self.tablero=tablero
        self.hijos=[]
    
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
                        self.hijos.append(Nodo(aux))
                    if(j<len(self.tablero)-1):
                        #hijo derecha
                        aux=np.zeros((len(self.tablero),len(self.tablero[i])),dtype=str)
                        aux[:][:]=self.tablero[:][:]
                        aux[i][j]=self.tablero[i][j+1]
                        aux[i][j+1]=self.tablero[i][j]
                        self.hijos.append(Nodo(aux))
                    if(i<len(self.tablero)-1):
                        #hijo abajo
                        aux=np.zeros((len(self.tablero),len(self.tablero[i])),dtype=str)
                        aux[:][:]=self.tablero[:][:]
                        aux[i][j]=self.tablero[i+1][j]
                        aux[i+1][j]=self.tablero[i][j]
                        self.hijos.append(Nodo(aux))
                    if(j>0):
                        #hijo izquierda
                        aux=np.zeros((len(self.tablero),len(self.tablero[i])),dtype=str)
                        aux[:][:]=self.tablero[:][:]
                        aux[i][j]=self.tablero[i][j-1]
                        aux[i][j-1]=self.tablero[i][j]
                        self.hijos.append(Nodo(aux))
    @staticmethod    
    def comprobar(nodo, objetivo):
        for i in range(len(nodo.tablero)):
            for j in range(len(nodo.tablero[i])):
                if(not nodo.tablero[i][j]==objetivo.tablero[i][j]):
                    return False
        return True
    def imprimir(self):
        print(self.tablero)
    
class NodoGranjero:
    def __init__(self,lado1,lado2,granjero):
        self.granjero=granjero
        self.lado1=lado1
        self.lado2=lado2
        self.hijos=[]

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
                    self.hijos.append(NodoGranjero(auxLado1,auxLado2,"derecha"))
            if(not self.comer(self.lado1)):
                auxLado1=[]
                auxLado1[:]=self.lado1[:]
                auxLado2=[]
                auxLado2[:]=self.lado2[:]
                self.hijos.append(NodoGranjero(auxLado1,auxLado2,"derecha")) 
        
        if(self.granjero=="derecha"):
            for n in self.lado2:
                auxLado1=[]
                auxLado1[:]=self.lado1[:]
                auxLado2=[]
                auxLado2[:]=self.lado2[:]

                auxLado1.append(n)
                auxLado2.remove(n)
                if(not self.comer(auxLado2)):
                    self.hijos.append(NodoGranjero(auxLado1,auxLado2,"izquierda"))
            if(not self.comer(self.lado2)):
                auxLado1=[]
                auxLado1[:]=self.lado1[:]
                auxLado2=[]
                auxLado2[:]=self.lado2[:]
                self.hijos.append(NodoGranjero(auxLado1,auxLado2,"izquierda"))
    @staticmethod    
    def comprobar(nodo, objetivo):
        for n in nodo.lado1:
            if not n in objetivo.lado1: return False
        for n in nodo.lado2:
            if not n in objetivo.lado2: return False
        if not nodo.granjero==objetivo.granjero: return False
        return True
    @staticmethod
    def comer(array):
        if array.__contains__("🐺") and array.__contains__("🐐"):
            return True
        if array.__contains__("🐐") and array.__contains__("🥬"):
            return True
        return False
    def imprimir(self):
        print(str(self.lado1)+" 🌊🌊🌊 " +str(self.lado2) +" Granjero en: "+self.granjero)

def profundidad(nodo, objetivo, limite):
    global encontrado
    global pila
    
    if(encontrado): return
    pila.append(nodo)

    if(limite==limiteProfundidad): return
    if(nodo.comprobar(nodo, objetivo)):
        encontrado=True
        return
    
    nodo.calculaHijos()
    for n in nodo.hijos:
        profundidad(n,objetivo,limite+1)
        if(not encontrado):
            pila.pop()


nodoOrigen=Nodo([['1','2','3'],['4','5','6'],['7','8','']])
nodoObjetivo=Nodo([['1','2','3'],['7','','4'],['8','6','5']])
# COMENTAR LAS SIGUIENTES DOS VARIABLES PARA EJECUTAR EL CODIGO DEL PUZZLE DESLIZANTE
nodoOrigen=NodoGranjero(["🐺","🥬","🐐"],[],"izquierda")
nodoObjetivo=NodoGranjero([],["🐺","🥬","🐐"],"derecha")


encontrado=False
pila=[]

profundidad(nodoOrigen, nodoObjetivo,0)

if(len(pila)==1): print("No se puede solucionar")
for n in pila:
    n.imprimir()
    print("---")