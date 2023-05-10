def juego(n):
    estanque=[]
    lado1="🐸"
    lado2="🐻"
    roca="🪨"

    for i in range(n):
        estanque.append(lado1)

    estanque.append(roca)

    for i in range(n):
        estanque.append(lado2)

    inicio=0
    fin=len(estanque)
    prueba=-1;

    def saltar(pos):
        estanque[estanque.index(roca)]=estanque[pos]
        estanque[pos]=roca

    while(inicio<n):
        print(estanque)
        
        if estanque[inicio]==lado2:
            inicio+=1;
        
        if estanque[fin-1]==lado1:
            fin=fin-1;
        
        espacio=estanque.index(roca)
        if (espacio==inicio):
            if estanque[espacio+1]==lado1:
                saltar(espacio+2)
            if estanque[espacio+1]==lado2:
                saltar(espacio+1)
            continue

        if (espacio==fin-1):
            if estanque[espacio-1]==lado1:
                saltar(espacio-1)
            if estanque[espacio-1]==lado2:
                saltar(espacio-2)
            continue

        if (estanque[espacio-1] == lado1) & (estanque[espacio+1] == lado1):
            saltar(espacio+2)
        if (estanque[espacio-1] == lado2) & (estanque[espacio+1] == lado2):
            saltar(espacio-2)
        if (estanque[espacio-1] == lado1) & (estanque[espacio+1] == lado2):
            saltar(espacio+prueba)
            prueba=prueba*-1
    print(estanque)

juego(3)