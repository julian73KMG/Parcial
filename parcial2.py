##Julian Mendez

#-- Problema 1 --
def elementoRepetido(v):
    for i in range(len(v)): #Recorre la palabra
        el = v[i]   #Guarda la letra, cambia con cada iteracion
        for j in range(i + 1,len(v)):   #Recorre, pero mirando desde la siguiente letra
            if el == v[j]:  #Si la iteracion coincide con la letra, devuelve True
                return True
    return False    #Si no coincide, devuelve False

#-- Problema 2 --
def hayVocales(v):
    s = 0   #Variable de suma
    for i in v: #Recorre la lista
        s = (i.count('a')  +  i.count('A') +    #contara las vocales en la palabra y sumara, asignando el valor a s 
            i.count('e')  +  i.count('E') +
            i.count('i')  +  i.count('I') +
            i.count('o')  +  i.count('O') +
            i.count('u')  +  i.count('U'))
        if s >= 2: #Si s es mayor o igual a 2 devuelve la palabra, sino, vuelve al for
            return i
    return 'No hay dos o más vocales'   #Si no hay 2 o más vocales devuelve el mensaje


#-- Problema 3 --
def difElementos(v,w):
    esta = [] #lista donde se guardaran los elementos diferentes
    for i in v: #Recorre la primer lista
        if i not in w:  #Si no esa en el segundo
            esta.append(i)  #Lo agrega
    return esta #Imprime

#-- Problema 4 --
def promedio(v):
    #Verificar que no este vacio
    if len(v) == 0:
        return 'Vacío'
    else:
        s = 0   #Variable de suma
        for i in range(len(v)): #Recorre el arreglo y suma cada indice
            s+=v[i]
        p = s/len(v)    #Calcula el promedio
    return p

#-- Problema 5 --
def mediana(v):
    #verificar que no esté vacío
    if len(v) == 0:
        return 'Vacío'
    else:
        v.sort()    #Ordenar el arreglo
        m = int(len(v)/2)    #Calcula mediana
        if len(v)%2==0: #Si es par la mediana es el numero calculado y el siguiente
            return v[m], v[m+1]
        else:
            return v[m]  #Si no es par, la mediana es el numero calculado


vacio = []
u = [1,2,3,4,5]
v = [3,2,1,4]
v1 = [3,2,1,4,5]
w = ['gat', 'pers', 'carro', 'raton']
w1 = ['gat', 'pers', 'carro', 'raton']
x = ['gat', 'pers', 'calle']
y = ['a', 's', 'x']
palabraTrue = 'rata'
palabraFalse = 'pato'

print(elementoRepetido(palabraFalse))
print(hayVocales(y))
print(difElementos(w,w1))
print(promedio(vacio))
print(mediana(v1))