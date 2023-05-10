lado1=["lobo","cabra","col"];
lado2=[];
respuesta=[];

def comprobar(array): #comprobamos que nada se coma a nada xd
    if array.__contains__("lobo") and array.__contains__("cabra"):
        return True
    if array.__contains__("cabra") and array.__contains__("col"):
        return True
    return False

while(True):
    respuesta.append("cruzar "+lado1[0]);
    lado2.append(lado1.pop(0));#pasamos el primero de la lista al otro lado
    if(len(lado2)==3):
        break
    if comprobar(lado1): #si algo se come a algo, lo regresamos al lado 1
        lado1.append(lado2.pop(0)); #correccion
        respuesta.pop();
    if comprobar(lado2): #si algo se come algo, regresamos el primero del lado 1
        respuesta.append("regresar "+lado2[0]);
        lado1.append(lado2.pop(0));

print(respuesta);