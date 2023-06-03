import numpy as np

inicio=1

tiles=10
ciudades=0

tabla=np.zeros((11,11),dtype=np.float32)
rueda=[1,7,3,8,2,10,4,9,6,5]

tabla[1][10]=11.72
tabla[1][2]=11.85
tabla[1][5]=3.13 #
tabla[1][7]=3.35 #

tabla[2][3]=9.22
tabla[2][8]=3.89 #
tabla[2][10]=4.37 #

tabla[3][4]=11.83
tabla[3][7]=3.03 #
tabla[3][8]=6.23 #

tabla[4][5]=6.77
tabla[4][9]=2.08 #
tabla[4][10]=5.66 #

tabla[5][6]=2.08

tabla[6][7]=7.92
tabla[6][9]=2.97 #

tabla[7][8]=8.62

tabla[8][9]=11.76

tabla[9][10]=7.41

#print(tabla)

escenario=None

principio=None
fin=None
abierta=[]
cerrada=[]
camino=[]

terminado=False

class Casilla:
    def __init__(self, pos):
        self.pos=pos
        #self.tipo=img[x][y]

        self.f=0
        self.g=0
        self.h=0

        self.vecinos=[]
        self.padre=None 
    
    def toString(self):
        return "ciudad " +str(self.pos+1)

def heuristica(a,b):
    n=abs(rueda.index(a.pos+1)-rueda.index(b.pos+1))

    return n

def borraArray(array, elemento):
    array.remove(elemento)
    #del array[elemento]


def algoritmo():
    global ciudades
    global terminado
    if(not terminado):
        if(len(abierta)>0):
            ganador=0
            for i in range(len(abierta)):
                if(abierta[i].f<abierta[ganador].f):
                    ganador=i
            actual=abierta[ganador]

            camino=[]
            temporal=actual
            camino.append(temporal)
            while(not temporal.padre==None):
                temporal=temporal.padre
                camino.append(temporal)

            if(len(camino)==9):
                n=0
                for i in reversed(camino):
                    print("vamos a "+i.toString() +" --- " +str(n))
                    n=n+1

                print("terminado")
                print("")
                terminado=True
            else:
                ciudades=ciudades+1
                borraArray(abierta, actual)
                cerrada.append(actual)
                

                vecinos=actual.vecinos
                for vecino in vecinos:
                    if((not vecino in cerrada)):
                        suma=tabla[actual.pos+1,vecino.pos+1]
                        if(suma==0):
                            suma=tabla[actual.pos+1,vecino.pos+1]
                        tempG=actual.g+suma
                        if(vecino in abierta):
                            if(tempG < vecino.g):
                                vecino.g=tempG
                        else:
                            vecino.g=tempG
                            abierta.append(vecino)
                        vecino.h=heuristica(actual, vecino)
                        vecino.f=vecino.g+vecino.h

                        vecino.padre=actual
                
        else:
            print("no hay solucion")
            terminado=True

escenario = [Casilla(i) for i in range(tiles)]
escenario[0].vecinos.append(escenario[9])
escenario[0].vecinos.append(escenario[1])
escenario[0].vecinos.append(escenario[4])
escenario[0].vecinos.append(escenario[6])

escenario[1].vecinos.append(escenario[0])
escenario[1].vecinos.append(escenario[2])
escenario[1].vecinos.append(escenario[7])
escenario[1].vecinos.append(escenario[9])

escenario[2].vecinos.append(escenario[1])
escenario[2].vecinos.append(escenario[3])
escenario[2].vecinos.append(escenario[6])
escenario[2].vecinos.append(escenario[7])

escenario[3].vecinos.append(escenario[2])
escenario[3].vecinos.append(escenario[4])
escenario[3].vecinos.append(escenario[8])
escenario[3].vecinos.append(escenario[9])

escenario[4].vecinos.append(escenario[3])
escenario[4].vecinos.append(escenario[5])
escenario[4].vecinos.append(escenario[0])

escenario[5].vecinos.append(escenario[4])
escenario[5].vecinos.append(escenario[6])
escenario[5].vecinos.append(escenario[8])

escenario[6].vecinos.append(escenario[5])
escenario[6].vecinos.append(escenario[7])
escenario[6].vecinos.append(escenario[0])
escenario[6].vecinos.append(escenario[2])

escenario[7].vecinos.append(escenario[6])
escenario[7].vecinos.append(escenario[8])
escenario[7].vecinos.append(escenario[2])
escenario[7].vecinos.append(escenario[1])

escenario[8].vecinos.append(escenario[7])
escenario[8].vecinos.append(escenario[9])
escenario[8].vecinos.append(escenario[5])
escenario[8].vecinos.append(escenario[3])

escenario[9].vecinos.append(escenario[8])
escenario[9].vecinos.append(escenario[0])
escenario[9].vecinos.append(escenario[3])
escenario[9].vecinos.append(escenario[1])

#principio=escenario[0][5]
principio=escenario[inicio-1]
abierta.append(principio)
'''
for i in escenario:
    for j in i:
        j.dibujaAbierta()
'''

#cv2.imshow("prueba",imagen)
#cv2.waitKey(0)



while(not terminado):
    algoritmo()


n=0
for i in reversed(camino):
        print("vamos a "+i.toString() +" --- " +str(n))
        n=n+1

print(ciudades)
