import cv2
#from google.colab.patches import cv2_imshow
#import cv2
import numpy as np

#solo funciona con laberintos cuadrados y mínimo con dos salidas, puede cambiar esas configuraciones en el generador
url="18161231b" #cambiar la url por la de su imagen (sin el ".png")

imagen=cv2.imread(url+".png")
if(not imagen):
    imagen=cv2.imread("2. Laberinto/"+url+".png")

tiles=[int(imagen.shape[1]/16),int(imagen.shape[0]/16)]
print(tiles)
img=np.zeros((tiles[1],tiles[0]),dtype=str)

pared="X"
espacio=" "

escenario=None

principio=None
fin=None
abierta=[]
cerrada=[]
camino=[]

terminado=False

class Casilla:
    def __init__(self, x,y):
        self.x=x
        self.y=y
        self.tipo=img[x][y]

        self.f=0
        self.g=0
        self.h=0

        self.vecinos=[]
        self.padre=None 
    
    def calculaVecinos(self):
        if(self.x>0):
            self.vecinos.append(escenario[self.x-1][self.y])#vecino izquierdo
        if(self.x<tiles[1]-1):
            self.vecinos.append(escenario[self.x+1][self.y])#vecino derecho
        if(self.y>0):
            self.vecinos.append(escenario[self.x][self.y-1])#vecino arriba
        if(self.y<tiles[0]-1):
            self.vecinos.append(escenario[self.x][self.y+1])#vecino derecho
    
    def dibujaAbierta(self):
        cv2.rectangle(imagen, (16*self.y,16*self.x), (16*self.y+16,16*self.x+16), (0,255,0), 2)
    def dibujaCerrada(self):
        cv2.rectangle(imagen, (16*self.y,16*self.x), (16*self.y+16,16*self.x+16), (0,0,255), 2)
    def dibujaCamino(self):
        cv2.rectangle(imagen, (16*self.y,16*self.x), (16*self.y+16,16*self.x+16), (255,0,0), 2)

    def toString(self):
        return "x: " +str(self.x) +" y: " +str(self.y)

def heuristica(a,b):
    x=abs(a.x-b.x)
    y=abs(a.y-b.y)

    return x+y

def borraArray(array, elemento):
    array.remove(elemento)
    #del array[elemento]

def getEscenario():
    #print(imagen[1*16+8][2*16+8][0]) img primero hacia abajo
    for i in range(tiles[1]):
        for j in range(tiles[0]):
            if(imagen[i*16+8][j*16+8][0]==255):
                img[i][j]=espacio
            else:
                img[i][j]=pared
    return img

def algoritmo():
    global terminado
    if(not terminado):
        if(len(abierta)>0):
            ganador=0
            for i in range(len(abierta)):
                if(abierta[i].f<abierta[ganador].f):
                    ganador=i
            actual=abierta[ganador]

            if(actual==fin):
                temporal=actual
                camino.append(temporal)
                while(not temporal.padre==None):
                    temporal=temporal.padre
                    camino.append(temporal)

                print("terminado")
                terminado=True
            else:
                borraArray(abierta, actual)
                cerrada.append(actual)

                vecinos=actual.vecinos
                for vecino in vecinos:
                    if((not vecino in cerrada) and (not vecino.tipo==pared)):
                        tempG=actual.g+1
                        if(vecino in abierta):
                            if(tempG < vecino.g):
                                vecino.g=tempG
                        else:
                            vecino.g=tempG
                            abierta.append(vecino)
                        vecino.h=heuristica(vecino, fin)
                        vecino.f=vecino.g+vecino.h

                        vecino.padre=actual
        else:
            print("no hay solucion")
            terminado=True

def seleccionaInicio():
    n=0
    entradas=[None, None]
    #print(escenario[50][64].tipo)########
    for i in range(tiles[0]):
        if(escenario[0][i].tipo==espacio):
            entradas[n]=escenario[0][i]
            n=n+1
        if(n==2):
            return entradas
    for i in range(tiles[1]):
        if(escenario[i][0].tipo==espacio):
            entradas[n]=escenario[i][0]
            n=n+1
        if(n==2):
            return entradas
    for i in range(tiles[0]):
        if(escenario[i][tiles[0]-1].tipo==espacio):
            entradas[n]=escenario[i][tiles[0]-1]
            n=n+1
        if(n==2):
            return entradas
    for i in range(tiles[1]):
        if(escenario[tiles[1]-1][i].tipo==espacio):
            entradas[n]=escenario[tiles[1]-1][i]
            n=n+1
        if(n==2):
            return entradas
    


img=getEscenario()
escenario = [[Casilla(i,j) for j in range(tiles[0])] for i in range(tiles[1])]

#principio=escenario[0][5]
principio=seleccionaInicio()[0]
fin=seleccionaInicio()[1]
abierta.append(principio)
for i in escenario:
    for j in i:
        j.calculaVecinos()
'''
for i in escenario:
    for j in i:
        j.dibujaAbierta()
'''

#cv2.imshow("prueba",imagen)
#cv2.waitKey(0)



while(not terminado):
    algoritmo()
    for i in cerrada:
        i.dibujaCerrada()
    for i in abierta:
        i.dibujaAbierta()

    cv2.imshow("laberinto",imagen)
    cv2.waitKey(1)

for i in camino:
        i.dibujaCamino()

imagen=cv2.resize(imagen,(680,680))
cv2.imshow("laberinto",imagen)
cv2.waitKey(0)