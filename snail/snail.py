def snail(n):
    k=0
    lista1 = []
    for i in range(n):
        lista1.append([])
    iterador =iter(range(1,n*n +1))
    Np = int(n)
    while True:
        if n == 1:
            lista1[Np//2].insert(Np//2, next(iterador))
            print(lista1)
            break
        #part1 LECT_ID
        for i in iter(range(n)):  
            lista1[k].insert(i+k,next(iterador))

        #part2 Elementos_aislados_D
        j=1+k
        for i in range(n-2):
            lista1[j].insert(len(lista1[j])//2,next(iterador))
            j +=1

        #part3 LECT_DI
        
        for i in range(n):
            if k >1:
                lista1[-1-k].insert(-(i+k),next(iterador))
            else:
                lista1[-1-k].insert(-(i+1),next(iterador))
       

        #part4 Elementos_aislados_I
        j=-2-k
        for i in range(n-2):
            lista1[j].insert(k,next(iterador))
            j-=1
    
        if n ==2:
            print(lista1)
            break    
        n -=2
        k+=1
    return lista1


for i in snail(9):
    print(i)
#hola mundo





