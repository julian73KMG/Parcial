##Julian Mendez
import math

#-- Problema 1 --
def elementoRepetido(v):
    for i in range(len(v)):
        el = v[i]
        for j in range(1,len(v)):
            if el == v[i]:
                r = True
            else: r = False
    return r

#-- Problema 2 --
def hayVocales(v):
    s = 0
    for i in range(0,len(v)):
        if s >= 2:
            r = v[i]
            return r
        else:
            r = 'No hay vocales'
            s += v[i].count('a')
            s += v[i].count('A')
            s += v[i].count('e')
            s += v[i].count('E')
            s += v[i].count('i')
            s += v[i].count('I')
            s += v[i].count('o')
            s += v[i].count('O')
            s += v[i].count('u')
            s += v[i].count('U')
            #print(s)
    return " "


#-- Problema 3 --
def difElementos(v,w):
    esta = "Se encuentra: "
    for i in range(len(v)):
        if v[i] != w[i]:
            esta += v[i]
    else:
        noesta = v[i]
    return esta

#-- Problema 4 --
def promedio(v):
    s = 0
    for i in range(len(v)):
        s+=v[i]
    p = s/len(v)

    return p

#-- Problema 5 --
def mediana(v):
    v.sort()
    m = len(v)/2
    if len(v)%2==0:
        m = int(m)
        return v[m], v[m+1]
    else:
        m = int(m)
        return v[m]


u=[1,2,3,4,5]
v=[3,2,1,4]
w=('gat', 'parica', 'carro')
x=('gat', 'perico', 'calle')

print(elementoRepetido('rata'))
print(hayVocales(x))
print(difElementos(w,x))
print(promedio(u))
print(mediana(v))
