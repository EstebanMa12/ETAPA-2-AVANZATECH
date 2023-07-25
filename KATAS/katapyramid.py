""" i = 0  
def position(n):
    lista1=[]
    iterador = range(1,n)
    while n not in lista1: """

lista1 =[]
listat = []
pA=1
def funcion(n):
    iterador = iter(range(1,n+1))

    def recursiva(p,iterador,listat):
        c = int(p)
        if c>=1:
            #print(next(iterador)) 
            try:
                listat.append(int(next(iterador)))
            except StopIteration as error:
                if listat != []:
                    lista1.append(listat)
                return lista1
            c-=1
            return recursiva(c,iterador,listat)

        lista1.append(listat) 
        listat = []
        global pA
        pA = pA+1
        return recursiva(pA,iterador,listat)


    lista = recursiva(pA,iterador,listat)
    listap = lista[-1]
    paso = len(lista)
    if len(lista)%2 ==0:
        if listap.index(n)>(paso/2)-1:
            return"D",lista
        else:
            return"L",lista
    else:
        if listap.index(n)>(paso//2):
            return "D",lista
        elif listap.index(n)==(paso//2):
            return "C",lista
        else:
            return "L",lista
        
print(funcion(19))

